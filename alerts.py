from datetime import datetime
import logging


def events(api):
    events = api.event.get({
        "output": "extend",
        "select_acknowledges": "extend",
        "selectTags": "extend",
        "selectSuppressionData": "extend",
        "sortfield": ["clock", "eventid"],
        "sortorder": "DESC"
    })

    print('\n==========================================')
    logging.warning("Listing events - [{}]".format(datetime.now()))
    for aux in events:

        print("\n******************************************")
        print("Name: {}".format(aux["name"]))
        print("Event ID: {}".format(aux["eventid"]))
        print("Serverity: {}".format(aux["severity"]))
        print("Source: {}".format(aux["source"]))
        print("Object: {}".format(aux["object"]))
        print("Object ID: {}".format(aux["objectid"]))
        print("Clock: {}".format(aux["clock"]))
        print("Value: {}".format(aux["value"]))
        print("Ns: {}".format(aux["ns"]))
        print("R_eventid: {}".format(aux["r_eventid"]))
        print("C_eventid: {}".format(aux["c_eventid"]))
        print("Correlationid: {}".format(aux["correlationid"]))
        print("Opdata: {}".format(aux["opdata"]))
        print("Suppressed: {}".format(aux["suppressed"]))
        print("Acknowledges: {}".format(aux["acknowledges"]))
        print("Suppression Data: {}".format(aux["suppression_data"]))
        print("URL: {}".format(aux["urls"]))
        print("Tags: {}".format(aux["tags"]))
        print("******************************************\n")
    logging.warning("End of listing events - [{}]".format(datetime.now()))
    print('\n==========================================')


def silence_alert(api):
    logging.warning("Silencing alerts - [{}]".format(datetime.now()))
    event = input("Enter the event ID: ")
    api.event.acknowledge({
        "eventids": event,
        "action": 16,
        "message": "Closing alert",
        "severity": 0
    })
    logging.warning("End of silencing alerts - [{}]".format(datetime.now()))


def no_silenced_alerts(api):

    events = api.event.get({
        "output": "extend",
        "select_acknowledges": "extend",
        "selectTags": "extend",
        "selectSuppressionData": "extend",
        "sortfield": ["clock", "eventid"],
        "sortorder": "DESC"
    })

    print('\n==========================================\n')
    logging.warning("Listing events - [{}]".format(datetime.now()))
    for aux in events:
        comp = str(aux["acknowledges"])
        if "'action': '16'" not in comp:
            print("\n******************************************")
            print("Name: {}".format(aux["name"]))
            print("Event ID: {}".format(aux["eventid"]))
            print("Serverity: {}".format(aux["severity"]))
            print("Source: {}".format(aux["source"]))
            print("Object: {}".format(aux["object"]))
            print("Object ID: {}".format(aux["objectid"]))
            print("Clock: {}".format(aux["clock"]))
            print("Value: {}".format(aux["value"]))
            print("Ns: {}".format(aux["ns"]))
            print("R_eventid: {}".format(aux["r_eventid"]))
            print("C_eventid: {}".format(aux["c_eventid"]))
            print("Correlationid: {}".format(aux["correlationid"]))
            print("Opdata: {}".format(aux["opdata"]))
            print("Suppressed: {}".format(aux["suppressed"]))
            print("Acknowledges: {}".format(aux["acknowledges"]))
            print("Suppression Data: {}".format(aux["suppression_data"]))
            print("URL: {}".format(aux["urls"]))
            print("Tags: {}".format(aux["tags"]))
            print("******************************************\n")
    logging.warning("End of listing events - [{}]".format(datetime.now()))
    print('\n==========================================')
