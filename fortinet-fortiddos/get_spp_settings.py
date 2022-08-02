""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME, RESOURCE_MAPPING
from .utils import MakeRestApiCall

logger = get_logger(LOGGER_NAME)


def get_spp_settings(config, params):
    resource_name = params.get('resource_name')
    resources = ["Access Control List", "Address Config", "Address Config IPv6"]
    if resource_name in resources:
        params.update({'resource_name': "SPP: {0}".format(resource_name)})
    spp = params.get('spp')
    ddos_conn = MakeRestApiCall(config)
    ep = "/api/v2/spp/{spp}/{resource_name}/".format(spp=spp,
                                                     resource_name=RESOURCE_MAPPING.get(resource_name, resource_name))
    response = ddos_conn.make_request(endpoint=ep)
    return response
