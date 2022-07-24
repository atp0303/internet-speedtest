# home-speedtest
Perform Ookla speed test and save results to influxdb

## Docker
General steps for building and pushing docker images
`docker build --build-arg base_image=python:3.10-bullseye --build-arg ookla_package=ookla-speedtest-1.1.1-linux-x86_64.tgz --no-cache -t atp33/internet-speedtest:0.2.0-x86_64 -t atp33/internet-speedtest:latest-x86_64 . && docker build --build-arg base_image=arm32v7/python:3.10-bullseye --build-arg ookla_package=ookla-speedtest-1.1.1-linux-armel.tgz -t atp33/internet-speedtest:0.2.0-arm32 --no-cache -t atp33/internet-speedtest:latest-arm32 --no-cache . && docker push atp33/internet-speedtest --all-tags`

## Usage

| Parameters  |  Values
|---|---
| INFLUXDB_SERVER  |   The server where influxdb is running e.g http://10.88.88.10:49161
| INFLUXDB_ORG  |   The organisation name of the influxdb instance which will hold the speedtest data
| INFLUXDB_BUCKET  |   The bucket name of the influxdb instance which will hold the speedtest data
| INFLUXDB_TOKEN  |   The influxdb API token with the read/write scope
| SPEEDTEST_INTERVAL  |   How often will the speed test be invoked.  Default value is 900 seconds

Enviroment variables can be overidden at runtime

```
docker run -d --name=internet-speedtest \
    -e INFLUXDB_SERVER=http://10.88.88.10:49161
	-e INFLUXDB_ORG=19B
	-e INFLUXDB_BUCKET=internet
	-e INFLUXDB_TOKEN=TOKEN	
	-e DEBUG=TRUE
	-e SPEEDTEST_INTERVAL "60"
    --restart always \
    atp33/internet-speedtest:latest-amd64
```

