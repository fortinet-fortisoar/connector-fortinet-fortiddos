""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .utils import MakeRestApiCall

logger = get_logger(LOGGER_NAME)


def delete_service_protection_profile_policy(config, params):
    ddos_conn = MakeRestApiCall(config)
    policy_name = params.get('policy_name')
    endpoint = "/api/v2/ddos/global/ddos_global_spp_policy/{policy_name}/".format(policy_name=policy_name)
    ddos_conn.headers.update({'Content-Type': 'application/json'})
    api_response = ddos_conn.make_request(method='DELETE', endpoint=endpoint)
    return {"status": "success",
            "message": "{0} deleted successfully.".format(policy_name)} if api_response == '' else {
        "status": "failed", "message": "Failed to delete {0}.".format(policy_name)}
