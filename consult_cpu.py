import logging
from datetime import datetime


def consult_cpu(api):
    # cat history used CPU
    print('\n==========================================')
    logging.warning("Consulting CPU - [{}]".format(datetime.now()))

    host = input("Enter hostid: ")
    histor = api.item.get({"output": "extend",
                           "hostids": host,
                           "search": {
                               "key_": "system"
                           },
                           "sortfield": "name"
                           })
    for aux in histor:
        print("\n******************************************")
        print("Name: {}".format(aux["name"]))
        print("Item ID: {}".format(aux["itemid"]))
        print("Host ID: {}".format(aux["hostid"]))
        print("Key: {}".format(aux["key_"]))
        print("Value: {}".format(aux["lastvalue"]))
        print("Last Clock: {}".format(aux["lastclock"]))
        print("History: {}".format(aux["history"]))
        print("Template: {}".format(aux["templateid"]))
        print("Lifetime: {}".format(aux["lifetime"]))
        print("Satus_codes: {}".format(aux["status"]))
        print("******************************************\n")
    logging.warning("CPU consulted - [{}]".format(datetime.now()))
    print('\n==========================================')
