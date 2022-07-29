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
    404: 'Not Found',
    "ssl_error": 'SSL certificate validation failed',
    'time_out': 'The request timed out while trying to connect to the remote server',
}


class MakeRestApiCall():
    def __init__(self, config):
        self.server_url = config.get('server_address').strip().strip('/')
        if not self.server_url.startswith('http') or not self.server_url.startswith('https'):
            self.server_url = 'https://' + self.server_url
        self.username = config.get("username")
        self.password = config.get("password")
        self.headers = {}
        self.verify_ssl = config.get("verify_ssl", True)
        self.__generate_token()

    def __generate_token(self):
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
                try:
                    return response.json()
                except:
                    return response.content.decode() if isinstance(response.content, bytes) else response.content
            else:
                logger.error("Error: {0} {1}".format(response.status_code, response.text))
                raise ConnectorError(
                    '{0} {1}'.format(response.status_code, error_msg.get(response.status_code, response.text)))
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
                else:
                    make_query.update({k: PARAM_MAPPING.get(v, v) if k in CONVERT_LIST else PARAM_MAPPING.get(k, k)})
        return '&'.join(make_query) if make_str else make_query
