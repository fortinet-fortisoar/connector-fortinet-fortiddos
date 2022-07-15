""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .utils import MakeRestApiCall

logger = get_logger(LOGGER_NAME)


def get_attack_information(config, params):
    ep = "/api/v2/drop_stats"
    # ep = "/api/v2/drop_stats?spp_name="+spp+"&subtype="+subtype+"&period="+period+"&dir="+direction
    # endpoint = "/api/v2/drop_stats?spp_name=SPP-0&subtype=top_attackers&period=1%20year&dir=Inbound"
    ddos_conn = MakeRestApiCall(config)
    query_str = ddos_conn.build_query(params, make_str=True)
    if query_str:
        ep += '?' + query_str
    response = ddos_conn.make_request(endpoint=ep)
    return response
