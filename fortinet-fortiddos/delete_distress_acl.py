""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .utils import MakeRestApiCall
logger = get_logger(LOGGER_NAME)


def get_distress_acl(ddos_conn, distress_acl_name):
    endpoint = "/api/v2/distress_acl/"
    acl_list = ddos_conn.make_request(endpoint=endpoint)
    acl_exist = list(filter(lambda x: x.get('mkey') == distress_acl_name, acl_list))
    return acl_exist


def delete_distress_acl(config, params):
    distress_acl_name = params.get("name")
    ddos_conn = MakeRestApiCall(config)
    acl_exist = get_distress_acl(ddos_conn, distress_acl_name)
    if not acl_exist:
        raise ConnectorError("{0} distress ACL name not exists.".format(distress_acl_name))
    endpoint = "/api/v2/distress_acl/?{name}".format(name=distress_acl_name)
    response = ddos_conn.make_request("DELETE", endpoint=endpoint)
    logger.debug('response: {0}'.format(response))
    return {"status": "success",
            "message": "{0} deleted successfully.".format(distress_acl_name)} if response == '' else {
        "status": "failed", "message": "Failed to delete {0}.".format(distress_acl_name)}
