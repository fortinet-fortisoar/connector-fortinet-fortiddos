""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from connectors.core.connector import Connector
from connectors.core.connector import get_logger, ConnectorError
from .builtins import *
from .constants import LOGGER_NAME
from .health_check import health_check
logger = get_logger(LOGGER_NAME)


class FortiDDos(Connector):
    def execute(self, config, operation, params, **kwargs):
        try:
            logger.info('In execute() Operation:[{}]'.format(operation))
            return supported_operations.get(operation)(config, params)
        except Exception as e:
            logger.exception(e)
            raise ConnectorError(e)

    def check_health(self, config):
        try:
            logger.info('starting health check')
            return health_check(config)
        except Exception as e:
            logger.exception(e)
            raise ConnectorError(e)
