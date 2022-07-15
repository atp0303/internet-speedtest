# home-speedtest
Perform Ookla speed test and save results to influxdb

## Installation
General install steps: https://github.com/influxdata/influxdb-client-python#installation

1. `pip install 'influxdb-client[ciso]' speedtest-cli --user`
2. `docker stop -f test && docker rm -f test` - optional
3. `docker build -t internetspeedtest:latest . && docker run --name test -t internetspeedtest:latest`



