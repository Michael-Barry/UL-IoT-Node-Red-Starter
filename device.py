#!/usr/local/bin/python
  
import sys
import json
import time
import random
import datetime
import ibmiotf.device

def getClient():
    try:
        options = {
                "org": "{ORG ID}",
                "type": "{DEVICE TYPE}",
                "id": "{DEVICE ID}",
                "auth-method": "token",
                "auth-token": "{TOKEN}"
                }
        client = ibmiotf.device.Client(options)
    except ibmiotf.ConnectionException  as e:
        print("exception connecting device: %s" % str(e))

    client.connect()
    return client

def getData():
    myWeather = {}
    myWeather["temp"] = random.randrange(14, 27)
    myWeather["time"] = datetime.datetime.now().strftime("%y-%m-%dT%H:%M:%S")
    myWeather["location"] = "ul"

    return myWeather


def publishData(client):
    myData = getData()
    print("{}".format(myData))
    client.publishEvent("TemperatureReading", "json", myData)


def main(argv=None):
    client = getClient()
    i = 0
    while i < 10:
        publishData(client)
        i = i + 1
        time.sleep(1 * 10)

if __name__ == "__main__":
    sys.exit(main())
