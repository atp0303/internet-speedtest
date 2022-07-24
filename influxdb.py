#!/usr/bin/env python
import os
import subprocess
import json
from pydoc import cli
import influxdb_client

from datetime import datetime

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

for key, value in os.environ.items():
    print('{}: {}'.format(key, value))


def getSpeedtestResults():
    process = subprocess.Popen(
        "/usr/local/bin/speedtest -f json --accept-license --accept-gdpr",
        shell=True,
        stdout=subprocess.PIPE)
    data = process.stdout.read().decode("utf8")
    return json.loads(data)


def push(influxServer, org, bucket, token, interval):
    import time as t
    while True:
        token = token
        org = org
        bucket = bucket
        timestamp = datetime.utcnow()

        response = getSpeedtestResults()
        print(response)
        with InfluxDBClient(url=influxServer, token=token, org=org) as client:
            body = [
                {
                    "measurement": "speedtest",
                    "time": timestamp,
                    "fields": {
                        "download": response["download"]["bandwidth"],
                        "upload": response["upload"]["bandwidth"],
                        "jitter": response["ping"]["jitter"],
                        "latency": response["ping"]["latency"],
                    }
                }
            ]
            write_api = client.write_api(write_options=SYNCHRONOUS)
            write_api.write(bucket=bucket, record=body)
            client.close()
        t.sleep(float(interval))


push(os.environ['INFLUXDB_SERVER'], os.environ['INFLUXDB_ORG'],
     os.environ['INFLUXDB_BUCKET'], os.environ['INFLUXDB_TOKEN'], os.environ['SPEEDTEST_INTERVAL'])
