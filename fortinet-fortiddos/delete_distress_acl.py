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
    distress_acl_name = params.get("name")
    endpoint = "/api/v2/distress_acl/?{name}".format(name=distress_acl_name)
    response = ddos_conn.make_request("DELETE", endpoint=endpoint)
    logger.debug('response: {0}'.format(response))
    return {"status": "success",
            "message": "{0} deleted successfully.".format(distress_acl_name)} if response == '' else {
        "status": "failed", "message": "Failed to delete {0}.".format(distress_acl_name)}
