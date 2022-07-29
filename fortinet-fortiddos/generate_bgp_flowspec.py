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


def generate_bgp_flowspec(config, params):
    content = {}
    ddos_conn = MakeRestApiCall(config)
    ddos_conn.headers.update({'Content-Type': 'application/json'})
    payload = ddos_conn.build_query(params)
    endpoint = "/api/v2/flowspec_generate"
    payload.update({
        'generate': 'enable'
    })
    payload_data = {'data': payload, 'mkey': -1}
    request_body = json.dumps(payload_data)
    response = ddos_conn.make_request("PUT", endpoint=endpoint, data=request_body)
    if response:
        logger.info("Successfully generated Flowspec")

    status_url = "/api/v2/flowspec_status"
    status_resp = ddos_conn.make_request("GET", status_url)

    if "Available" in status_resp["report-status"]:
        download_url = "/api/v2/flowspec_config"
        ddos_conn.headers.update({'Accept': 'text/plain', 'Content-Type': 'application/json'})
        download_resp = ddos_conn.make_request("GET", download_url)
        content.update({'data': download_resp})
        # content = content.replace('\n', " ")
        # content = content.replace('\t', " ")
    return content
