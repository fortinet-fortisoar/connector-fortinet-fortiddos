""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .utils import MakeRestApiCall
import json

logger = get_logger(LOGGER_NAME)


def add_lq(config, params):
    ddos_conn = MakeRestApiCall(config)
    data = ddos_conn.build_query(params)
    request_body = {'data': data}
    rq = json.dumps(request_body)
    endpoint = "/api/v2/legitimate_queries/"
    ddos_conn.headers.update({'Content-Type': 'application/json'})
    api_response = ddos_conn.make_request(method='POST', endpoint=endpoint, data=rq)
    return api_response
