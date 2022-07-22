from datetime import datetime
import login
import logging
import host
import alerts
import consult_cpu


if __name__ == "__main__":

    # MENU APLICATION
    api = login.connect_zabbix()
    logging.warning(
        'Connected to Zabbix API Version {} - [{}]'.format(api.api_version(), datetime.now()))

    opt = 0
    while opt != 7:
        print("""
        1. Add a new Host
        2. Remove a Host
        3. List all alerts
        4. Silence an alert
        5. List all not silenced alerts
        6. Consult CPU
        7. Exit
        """)
        opt = int(input("Enter an option: "))
        if opt == 1:
            host.create_host(api)
        elif opt == 2:
            host.remove_host(api)
        elif opt == 3:
            alerts.events(api)
        elif opt == 4:
            alerts.silence_alert(api)
        elif opt == 5:
            alerts.no_silenced_alerts(api)
        elif opt == 6:
            consult_cpu.consult_cpu(api)
        elif opt == 7:
            print("")
            logging.warning("Exiting...[{}]".format(datetime.now()))
            break
        else:
            print("Invalid option")
            print("Please try again")
            print("")
            continue
