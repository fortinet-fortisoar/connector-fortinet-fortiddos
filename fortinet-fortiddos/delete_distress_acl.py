""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .utils import MakeRestApiCall


logger = get_logger(LOGGER_NAME)


def delete_distress_acl(config, params):
    ddos_conn = MakeRestApiCall(config)
    endpoint = "/api/v2/distress_acl/?{name}".format(name=params.get("name"))
    response = ddos_conn.make_request("DELETE", endpoint=endpoint)
    return response
