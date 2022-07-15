""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from connectors.core.connector import get_logger, ConnectorError
from .constants import *
import requests
import json

logger = get_logger(LOGGER_NAME)

error_msg = {
    401: 'Authentication failed due to invalid credentials',
    429: 'Rate limit was exceeded',
    403: 'Token is invalid or expired',
    "ssl_error": 'SSL certificate validation failed',
    'time_out': 'The request timed out while trying to connect to the remote server',
}


class MakeRestApiCall():
    def __init__(self, config):
        logger.info("config: {}".format(config))
        self.server_url = config.get('server_address').strip().strip('/')
        if not self.server_url.startswith('http') or not self.server_url.startswith('https'):
            self.server_url = 'https://' + self.server_url
        self.username = config.get("username")
        self.password = config.get("password")
        self.headers = {}
        # self.headers["Content-Type"] = "application/json"
        self.verify_ssl = config.get("verify_ssl", True)
        self.__generate_token()


    def __generate_token(self):
        # curl -H "ContentType:application/json" -X POST -d ' {"username":"rest_api_admin","password":"rest_api_password"}' https://172.30.153.169/api/authenticate/ -k
        self.headers = {"ContentType": "application/json"}
        data = {"username": self.username, "password": self.password}
        endpoint = '/api/authenticate/'
        token = self.make_request(method='POST', endpoint=endpoint, data=json.dumps(data)).get('access_token')
        self.headers["Authorization"] = "Bearer " + token

    def make_request(self, method='GET', endpoint='', params=None, data=None, json_data=None):
        try:
            if "Accept" not in self.headers:
                self.headers["Accept"] = "application/json"
            url = self.server_url + endpoint
            logger.debug('endpoint url:{0}'.format(url))
            response = requests.request(method=method, url=url, headers=self.headers, data=data, json=json_data,
                                        params=params, verify=self.verify_ssl)

            if response.ok:
                if 'json' in str(response.headers):
                    return response.json()
                else:
                    return response.text
            else:
                logger.error("Error: {0}".format(response.json()))
                raise ConnectorError('{0}'.format(error_msg.get(response.status_code, response.text)))
        except requests.exceptions.SSLError as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(error_msg.get('ssl_error')))
        except requests.exceptions.ConnectionError as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(error_msg.get('time_out')))
        except Exception as e:
            logger.error('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))

    def build_query(self, params, make_str=False):
        make_query = [] if make_str else {}
        for k, v in params.items():
            if v is not None and v != '':
                if k in CONVERT_STR:
                    v = str(v)
                if make_str:
                    query = "{k}={v}".format(k=k, v=v)
                    make_query.append(query)
                make_query.update({k: PARAM_MAPPING.get(v) if k in CONVERT_LIST else PARAM_MAPPING.get(k, k)})
        return '&'.join(make_query) if make_str else make_query


