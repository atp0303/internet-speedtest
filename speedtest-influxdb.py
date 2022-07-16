#!/usr/bin/env python
import os
from pydoc import cli
import influxdb_client
import speedtest

from datetime import datetime

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

for key, value in os.environ.items():
    print('{}: {}'.format(key, value))


def push(influxServer, org, bucket, token, interval):
    import time as t
    while True:
        token = token
        org = org
        bucket = bucket
        timestamp = datetime.utcnow()

        # run a single-threaded speedtest using default server
        s = speedtest.Speedtest()
        s.get_best_server()
        s.download(threads=1)
        s.upload(threads=1)
        res = s.results.dict()
        print(res)

        with InfluxDBClient(url=influxServer, token=token, org=org) as client:
            body = [
                {
                    "measurement": "speedtest",
                    "time": timestamp,
                    "fields": {
                        "download": res["download"],
                        "upload": res["upload"],
                        "ping": res["ping"]
                    }
                }
            ]
            write_api = client.write_api(write_options=SYNCHRONOUS)
            write_api.write(bucket=bucket, record=body)
            client.close()
        t.sleep(float(interval))


push(os.environ['INFLUXDB_SERVER'], os.environ['INFLUXDB_ORG'],
     os.environ['INFLUXDB_BUCKET'], os.environ['INFLUXDB_TOKEN'], os.environ['SPEEDTEST_INTERVAL'])
