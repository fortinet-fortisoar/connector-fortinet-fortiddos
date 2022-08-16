""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME, RESOURCE_MAPPING
from .utils import MakeRestApiCall

logger = get_logger(LOGGER_NAME)


def get_global_settings(config, params):
    logger.info("params: {}".format(params))
    resource_name = params.get('resource_name', None)
    if not resource_name:
        resource_name = 'ddos_global_setting'
    ddos_conn = MakeRestApiCall(config)
    ep = "/api/v2/" + (
        'distress_acl/' if resource_name == 'Advanced Settings: Distress ACL' else 'ddos/global/{resource_name}/'.format(
            resource_name=RESOURCE_MAPPING.get(resource_name, resource_name)))
    response = ddos_conn.make_request(endpoint=ep)
    return response


def get_bypass_mac(config, params):
    params.update({'resource_name': 'ddos_global_bypass_macs'})
    return get_global_settings(config, params)


def get_proxy_ip_policy(config, params):
    params.update({'resource_name': 'ddos_global_proxyip_policy'})
    return get_global_settings(config, params)


def get_proxy_ip(config, params):
    params.update({'resource_name': 'ddos_global_proxy_ip'})
    return get_global_settings(config, params)


def get_domain_reputation(config, params):
    params.update({'resource_name': 'ddos_global_domain_reputation'})
    return get_global_settings(config, params)


def get_ip_reputation(config, params):
    params.update({'resource_name': 'ddos_global_ipreputation'})
    return get_global_settings(config, params)
