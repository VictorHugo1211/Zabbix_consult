from datetime import datetime
import logging
import time


def create_host(api):
    logging.warning("Creating host - [{}]".format(datetime.now()))
    host_name = input("Enter host name: ")
    host_ip = input("Enter host IP: ")
    host_group = input("Enter host group: ")
    host_template = input("Enter host template: ")
    hostcriado = api.host.create({
        "host": "{}".format(host_name),
        "status": 0,  # desabilitado
        "interfaces": [{
            "type": 1,  # agente
            "main": 1,
            "useip": 1,
            "ip": "{}".format(host_ip),
            "dns": "",
            "port": 10050
        }],
        "groups": [{
            "groupid": "{}".format(host_group)  # Linux servers
        }],
        "templates": [{
            "templateid": "{}".format(host_template)  # Template Linux
        }]
    })
    time.sleep(2)
    x = (hostcriado["hostids"][0])
    print('\n==========================================')
    logging.warning("Host created with ID {} - [{}]".format(x, datetime.now()))
    print('==========================================\n')


def remove_host(api):
    logging.warning("Removing host - [{}]".format(datetime.now()))
    host_id = input("Enter host ID: ")
    api.host.delete([host_id])
    print('\n==========================================')
    logging.warning(
        "Host removed with ID {} - [{}]".format(host_id, datetime.now()))
    print('==========================================\n')
