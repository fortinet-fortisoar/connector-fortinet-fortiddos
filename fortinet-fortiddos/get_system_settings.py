""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .utils import MakeRestApiCall

logger = get_logger(LOGGER_NAME)


def get_system_settings(config, params):
    resource_name = params.get('resource_name')
    ddos_conn = MakeRestApiCall(config)
    ep = "api/v2/system/{0}".format(resource_name)
    response = ddos_conn.make_request(endpoint=ep)
    return response
