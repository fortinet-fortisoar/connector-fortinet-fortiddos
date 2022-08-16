""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from .get_spp_settings import get_spp_settings
from .get_global_settings import *
from .get_system_settings import get_system_settings
from .get_log_settings import get_log_settings
from .get_attack_information import get_attack_information
from .add_distress_acl import add_distress_acl
from .add_service_protection_profile_policy import add_service_protection_profile_policy
from .update_service_protection_profile_settings import update_service_protection_profile_settings
from .add_lq import add_lq
from .delete_lq import delete_lq
from .delete_service_protection_profile_policy import delete_service_protection_profile_policy
from .delete_distress_acl import delete_distress_acl
from .generate_bgp_flowspec import generate_bgp_flowspec
from .get_service_protection_profile_policy import  get_service_protection_profile_policy

supported_operations = {'get_spp_settings': get_spp_settings,
                        'get_global_settings': get_global_settings,
                        'get_global_spp': get_global_settings,
                        'get_settings': get_global_settings,
                        'get_global_settings_address': get_global_settings,
                        'get_ip_reputation': get_ip_reputation,
                        'get_domain_reputation': get_domain_reputation,
                        'get_proxy_ip': get_proxy_ip,
                        'get_proxy_ip_policy': get_proxy_ip_policy,
                        'get_do_not_track_policy': get_global_settings,
                        'get_global_acl': get_global_settings,
                        'get_bypass_mac': get_bypass_mac,


                        'get_system_settings': get_system_settings,
                        'get_log_settings': get_log_settings,


                        'get_attack_information': get_attack_information,
                        'add_distress_acl': add_distress_acl,
                        'add_service_protection_profile_policy': add_service_protection_profile_policy,
                        'get_service_protection_profile_policy': get_service_protection_profile_policy,
                        'update_service_protection_profile_settings': update_service_protection_profile_settings,
                        'add_lq': add_lq,
                        'delete_lq': delete_lq,
                        'delete_service_protection_profile_policy': delete_service_protection_profile_policy,
                        'delete_distress_acl': delete_distress_acl,
                        'generate_bgp_flowspec': generate_bgp_flowspec}
