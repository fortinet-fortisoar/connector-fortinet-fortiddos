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


def add_distress_acl(config, params):
    mkey = params.get('mkey')
    ddos_conn = MakeRestApiCall(config)
    data = ddos_conn.build_query(params)
    ddos_conn.headers.update({'Content-Type': 'application/json'})
    ep = "/api/v2/distress_acl/"
    data['system-generated'] = 'disable'
    if data.get('destination') == 'spp':
        data.pop('destination')
    request_body = {'data': data}
    rq = json.dumps(request_body)
    api_response = ddos_conn.make_request(method='POST', endpoint=ep, data=rq)
    return {"status": "success",
            "message": "{0} created successfully.".format(mkey)} if api_response == '' else {
        "status": "failed", "message": "Failed to create {0}.".format(mkey)}
