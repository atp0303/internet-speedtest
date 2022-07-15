FROM python:3.10
LABEL MAINTAINER=atp0303@hotmail.com
ADD speedtest-influxdb.py /root/./home/speedtest-influxdb.py

ENV INFLUXDB_SERVER "http://10.88.88.10:49161"
ENV INFLUXDB_ORG "19B"
ENV INFLUXDB_BUCKET "internet"
ENV INFLUXDB_TOKEN "P27mKSa_0FEMZPpJPRaSRKRwNgR6zszfjdVspasBXA98Ib4veDnFgs2DN91YeU3ha6L3vE6L3czLIbbeaOaW3Q=="
ENV SPEEDTEST_INTERVAL "60"
ENV DEBUG "FALSE"
RUN apt-get -y update
#RUN apt-get -y install cron
RUN python3 -m pip install 'influxdb-client[ciso]'
RUN python3 -m pip install speedtest-cli

# Copy file to the cron.d directory
#COPY speedtest-cron /etc/cron.d/speedtest-cron

# Give execution rights on the cron job
#RUN chmod 0644 /etc/cron.d/speedtest-cron

# Apply cron job
#RUN crontab /etc/cron.d/speedtest-cron

# Create the log file to be able to run tail
#RUN touch /var/log/cron.log

# Run the command on container startup
#CMD cron && tail -f /var/log/cron.log && python3 setup.py install --user
CMD python3 /root/./home/speedtest-influxdb.py
