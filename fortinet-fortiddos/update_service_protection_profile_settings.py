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
    resource_name = params.get('resource_name')
    response = get_spp_settings(config, params)
    spp_args = params.get('parameter_name_val')
    if not response.get('data'):
        raise ConnectorError('No data for "{}" resource.'.format(resource_name))
    data = response.get('data')[0]
    data.update(spp_args)
    request_body = {'data': data}
    rq = json.dumps(request_body)
    ddos_conn = MakeRestApiCall(config)
    ddos_conn.headers.update({'Accept': '*/*', 'Content-Type': 'application/json'})
    spp = params.get('spp')
    endpoint = "/api/v2/spp/{spp_name}/ddos_spp_setting/".format(spp_name=spp)
    api_response = ddos_conn.make_request(method='PUT', endpoint=endpoint, data=rq)
    return {"status": "success",
            "message": "{0} updated successfully.".format(resource_name)} if api_response == '' else {
        "status": "failed", "message": "Failed to update {0}.".format(resource_name)}
