""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
LOGGER_NAME = 'fortinet-fortiddos'
CONVERT_LIST = ['alt-spp-enable', 'acl-enable', 'destination-port', 'dscp', 'fragment', 'protocol', 'source-ip',
                'source-port', 'tcp-control-flag', 'ttl']
CONVERT_STR = ['destination-port-end', 'threshold-per-million', 'protocol-number', 'ttl-value', 'class', 'threshold',
               'subnet-id', 'destination-port-start', 'source-port-start', 'source-port-end', 'dscp-value']
PARAM_MAPPING = {
    True: 'enable',
    False: 'disable',
    'first-fragment': '1',
    'non-fragment-or-first-fragment': '2',
    'not-first-fragment': '3',
    'any-fragment': '4',

    # destination
    'ip-netmask-ipv4': '1',
    'all': '4'
}
RESOURCE_MAPPING = {
    #Protection Profiles Resource Mapping
    'SPP Settings': 'ddos_spp_setting',
    "Service Config": "ddos_spp_firewall_service",
    "SPP: Access Control List": "ddos_spp_firewall_policy",
    "SPP: Address Config": "ddos_spp_firewall_address",
    "SPP: Address Config IPv6": "ddos_spp_firewall_address6",
    "Extended Timeout Policy": "ddos_spp_tcp_session_extended_timeout_policy",
    "Thresholds > Thresholds > Scalars": "ddos_spp_threshold_scalar",
    "Thresholds > Thresholds > HTTP Methods": "ddos_spp_threshold_http_methods",
    "Thresholds > Thresholds > Protocols": "ddos_spp_threshold_protocol",
    "Thresholds > Thresholds > TCP Ports": "ddos_spp_threshold_tcp_ports",
    "Thresholds > Thresholds > UDP Ports":"ddos_spp_threshold_udp_ports",
    "Thresholds > Thresholds > ICMP Types/Codes": "ddos_spp_threshold_icmp_type_codes",
    "Thresholds > Thresholds > URLs": "ddos_spp_threshold_http_urls",
    "Thresholds > Thresholds > Hosts": "ddos_spp_threshold_http_hosts",
    "Thresholds > Thresholds > Referers": "ddos_spp_threshold_http_referers",
    "Thresholds > Thresholds > Cookies": "ddos_spp_threshold_http_cookies",
    "Thresholds > Thresholds > User Agents": "ddos_spp_threshold_http_user_agents",

    #Global Settings Mapping
    "Switching Policy": "ddos-global-spp-switching-policy",
    "SPP Policy": "ddos-global-spp-policy",
    "SPP Policy Group": "ddos_global_spp_policy_group",

    "HTTP Service Ports": "ddos_global_http_service_ports",
    "UDP Service Ports": "ddos_global_udp_service_ports",
    "Signaling": "ddos_global_sp_fdd",
    "GRE Tunnel Endpoint": "ddos_global_service_provider_address",

    "Local Address Config": "ddos_global_firewall_local_address",
    "Local Address Config IPv6": "ddos_global_firewall_local_address6",
    "Address Config": "ddos_global_firewall_address",
    "Address Config IPv6": "ddos_global_firewall_address6",

    "Do Not Track Policy": "ddos_global_do_not_track_policy",
    "Do Not Track Policy IPv6": "ddos_global_do_not_track_policy6",

    "Access Control List": "ddos_global_firewall_policy",
    "Access Control List IPv6": "ddos_global_firewall_policy6",
    "Advanced Settings: Distress ACL": "ddos_global_distress_acl",

    #System Settings Mapping
    "Interface": "interface",
    "DNS": "dns",
    "Static Route": "route",
    "High Availability": "HA",
    "System Information": "snmp_sysinfo",
    "SNMP Threshold": "snmp_threshold",
    "Community": "snmp_community",

    "Auth Radius": "auth_radius",
    "Auth LDAP": "auth_LDAP",
    "Auth TACACS+": "auth_tacacsplus",

    "Admin User": "adminuser",
    "Access Profile": "accprofile",
    "Settings": "sysglobal",
    "Certificate": "certificate_local"
}

error_msg = {
    401: 'Authentication failed due to invalid credentials',
    404: 'Not Found',
    405: 'Method not allowed',
    "ssl_error": 'SSL certificate validation failed',
    'time_out': 'The request timed out while trying to connect to the remote server',
}

resources = ["Access Control List", "Address Config", "Address Config IPv6"]