""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .get_spp_settings import get_spp_settings
from .utils import MakeRestApiCall
import json

logger = get_logger(LOGGER_NAME)


def update_service_protection_profile_settings(config, params):
    response = get_spp_settings(config, params)
    spp_args = params.get('parameter_name_val')
    data = response.get('data')
    data[0].update(spp_args)
    request_body = {'data': data}
    rq = json.dumps(request_body)
    ddos_conn = MakeRestApiCall(config)
    ddos_conn.headers = {'Accept': '*/*', 'Content-Type': 'application/json'}
    spp = params.get('spp')
    endpoint = "/api/v2/spp/{spp_name}/ddos_spp_setting/".format(spp_name=spp)
    api_response = ddos_conn.make_request(method='PUT', endpoint=endpoint, data=rq)
    return api_response
    