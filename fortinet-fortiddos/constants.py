""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
LOGGER_NAME = 'fortinet-fortiddos'
CONVERT_LIST = ['alt-spp-enable', 'acl-enable', 'destination-port', 'dscp', 'fragment', 'protocol', 'source-ip', 'source-port', 'tcp-control-flag', 'ttl']
CONVERT_STR = ['destination-port-end', 'threshold-per-million', 'protocol-number', 'ttl-value', 'class', 'threshold']
PARAM_MAPPING = {
    True: 'enable',
    False: 'disable',
    'first-fragment': '1',
    'non-fragment-or-first-fragment': '2',
    'not-first-fragment': '3',
    'any-fragment': '4',

     #destination
    'ip-netmask-ipv4': '1',
    'all': '4'




}
