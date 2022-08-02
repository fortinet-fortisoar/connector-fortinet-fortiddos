""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
import json
from .utils import MakeRestApiCall

logger = get_logger(LOGGER_NAME)


def add_service_protection_profile_policy(config, params):
    mkey = params.get('mkey')
    ddos_conn = MakeRestApiCall(config)
    ddos_conn.headers.update({'Accept': '*/*', 'Content-Type': 'application/json'})
    data = ddos_conn.build_query(params)
    ep = "/api/v2/ddos/global/ddos_global_spp_policy/"
    if data.get('alt-spp-enable') == 'disable':
        data['alt-spp'] = ''
    if data.get('ip-version') == 'IPv4':
        data['ipv6-addr-prefix'] = "::/0"
    else:
        data['ip-addr-mask'] = "0.0.0.0/0"
    data['comment'] = 'Added via FortiSOAR' if not data.get('comment') else data.get('comment')
    request_body = {'data': data}
    rq = json.dumps(request_body)
    api_response = ddos_conn.make_request(method='POST', endpoint=ep, data=rq)
    return {"status": "success",
            "message": "{0} created successfully.".format(mkey)} if api_response == '' else {
        "status": "failed", "message": "Failed to create {0}.".format(mkey)}