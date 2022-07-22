import logging
from zabbix_api import ZabbixAPI
from datetime import datetime
import configparser


def connect_zabbix():
    logging.warning("Connecting to Zabbix API - [{}]".format(datetime.now()))
    config = configparser.ConfigParser()
    config.read("config.ini")
    zabbix_url = config.get("zabbix", "server")
    zabbix_user = config.get("zabbix", "user")
    zabbix_password = config.get("zabbix", "password")

    zapi = ZabbixAPI(zabbix_url)
    zapi.session.verify = False
    zapi.login(zabbix_user, zabbix_password)

    return zapi
