ARG base_image=python:3.10-bullseye
FROM ${base_image}
LABEL MAINTAINER=atp0303@hotmail.com
ADD influxdb.py /internet-speedtest/influxdb.py

ENV INFLUXDB_SERVER="http://10.88.88.10:49161"
ENV INFLUXDB_ORG="19B"
ENV INFLUXDB_BUCKET="internet"
ENV INFLUXDB_TOKEN=""
ENV SPEEDTEST_INTERVAL="900"

RUN apt-get -y update
RUN python3 -m pip install 'influxdb-client[ciso]'
ARG ookla_package=ookla-speedtest-1.1.1-linux-x86_64.tgz
RUN apt-get -y update
RUN apt-get install wget -y
RUN wget https://install.speedtest.net/app/cli/${ookla_package}
RUN tar -xvzf ${ookla_package}
RUN mv speedtest /usr/bin/speedtest

CMD python3 /internet-speedtest/influxdb.py
