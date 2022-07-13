#!/usr/bin/env python
import sys
from pydoc import cli
import influxdb_client
import speedtest

from datetime import datetime

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

print(sys.argv[0])


def push(influxInstance, org, bucket, token):
    # You can generate an API token from the "API Tokens Tab" in the UI
    token = token
    org = org
    bucket = bucket
    time = datetime.utcnow()

    # run a single-threaded speedtest using default server
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download(threads=1)
    s.upload(threads=1)
    res = s.results.dict()

    with InfluxDBClient(url=influxInstance, token=token, org=org) as client:
        print(res)
        body = [
            {
                "measurement": "speedtest",
                "time": time,
                "fields": {
                    "download": res["download"],
                    "upload": res["upload"],
                    "ping": res["ping"]
                }
            }
        ]
        write_api = client.write_api(write_options=SYNCHRONOUS)
        query_api = client.query_api()
        write_api.write(bucket=bucket, record=body)
        client.close()
