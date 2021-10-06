#!/usr/bin/env python3
import requests
from datetime import datetime, timedelta
import time
from requests.exceptions import Timeout

headers = {
    'cookie': "OwnerID=\"32772\""
    }

def getTimeString():
    now = datetime.now( )
    plctime =  now - datetime(1601, 1, 1, 0, 0, 0) + timedelta(hours=3) #referencia 1601 + timezone -3
    plctime_hex = (hex(int(plctime.total_seconds()*1e7)))
    plctime_string = str("0x") + str(plctime_hex[-8:]) + str("|0x0") + str(plctime_hex[2:-8])

    return plctime_string

def main(ip):
    url = "http://" + ip + "/setlst.cgi"

    payload = "var=C-0-0050.0.0.7&values=" + getTimeString()
    try:
        response = requests.request("POST", url, data=payload, headers=headers, timeout=3)
    except:
        print("Estação " + ip + " -> " + "exception")  # Python 3.6
        pass
    else:
        print("Estação " + ip + " -> " + str(response.text))

if __name__ == "__main__":

    plcList = ["172.20.8.100", "172.20.8.101", "172.20.8.102", "172.20.8.103"]

    while True:
        for plc in plcList:
            main(plc)

        time.sleep(600)
            




