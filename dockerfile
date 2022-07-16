FROM python:3.10
LABEL MAINTAINER=atp0303@hotmail.com
ADD speedtest-influxdb.py /root/./home/speedtest-influxdb.py

ENV INFLUXDB_SERVER "http://10.88.88.10:49161"
ENV INFLUXDB_ORG "19B"
ENV INFLUXDB_BUCKET "internet"
ENV INFLUXDB_TOKEN "P27mKSa_0FEMZPpJPRaSRKRwNgR6zszfjdVspasBXA98Ib4veDnFgs2DN91YeU3ha6L3vE6L3czLIbbeaOaW3Q=="
ENV SPEEDTEST_INTERVAL "900"
ENV DEBUG "FALSE"

RUN apt-get -y update
RUN python3 -m pip install 'influxdb-client[ciso]'
RUN python3 -m pip install speedtest-cli

CMD python3 /root/./home/speedtest-influxdb.py
