""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .utils import MakeRestApiCall

logger = get_logger(LOGGER_NAME)


def get_service_protection_profile_policy(config, params):
    ddos_conn = MakeRestApiCall(config)
    ep = "/api/v2/ddos/global/ddos_global_spp_policy/"
    response = ddos_conn.make_request(endpoint=ep)
    return response
