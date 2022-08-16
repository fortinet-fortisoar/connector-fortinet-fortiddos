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
    query = params.get('query')
    ddos_conn = MakeRestApiCall(config)
    data = ddos_conn.build_query(params)
    request_body = {'data': data}
    rq = json.dumps(request_body)
    endpoint = "/api/v2/legitimate_queries/"
    api_response = ddos_conn.make_request(method='POST', endpoint=endpoint, data=rq)
    return {"status": "success",
            "message": "{0} created successfully.".format(query)} if api_response == '' else {
        "status": "failed", "message": "Failed to create {0}.".format(query)}
