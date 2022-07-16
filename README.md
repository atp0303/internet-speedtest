# home-speedtest
Perform Ookla speed test and save results to influxdb

## Installation
General install steps: https://github.com/influxdata/influxdb-client-python#installation

1. `pip install 'influxdb-client[ciso]' speedtest-cli --user`
2. `docker stop -f test && docker rm -f test` - optional
3. `docker build -t atp33/internet-speedtest:0.1.0`
4. `docker run --name test -t internetspeedtest:latest`

## Running

| Parameters  |  Values
|---|---
| INFLUXDB_SERVER  |   The server where influxdb is running e.g http://10.88.88.10:49161
| INFLUXDB_ORG  |   The organisation name of the influxdb instance which will hold the speedtest data
| INFLUXDB_BUCKET  |   The bucket name of the influxdb instance which will hold the speedtest data
| INFLUXDB_TOKEN  |   The influxdb API token with the read/write scope
| SPEEDTEST_INTERVAL  |   How often will the speed test be invoked.  Default value is 900 seconds
| DEBUG  |   Display diagnostics data in the terminal.  Default value is false.


