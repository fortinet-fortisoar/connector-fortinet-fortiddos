""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .utils import MakeRestApiCall

logger = get_logger(LOGGER_NAME)


def delete_lq(config, params):
    query = params.get('query')
    type = params.get('type')
    class_val = str(params.get('class'))
    ddos_conn = MakeRestApiCall(config)
    endpoint = "/api/v2/legitimate_queries/?{query},{type},{class_val}".format(query=query, type=type,
                                                                               class_val=class_val)
    ddos_conn.headers = {'Content-Type': 'application/json'}
    api_response = ddos_conn.make_request(method='DELETE', endpoint=endpoint)
    return api_response
