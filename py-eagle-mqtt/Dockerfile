ARG BUILD_FROM
FROM $BUILD_FROM

LABEL io.hass.version="VERSION" io.hass.type="addon" io.hass.arch="armhf|aarch64|i386|amd64"

ENV LANG C.UTF-8

# Install requirements for add-on
RUN apk add --no-cache python3

WORKDIR /app
COPY ./src /app/src
COPY ./requirements.txt /app
COPY ./src/conf/logrotate/tHome /etc/logrotate.d/

ENV PYTHONPATH=/app/src/python
RUN apk --update add --no-cache logrotate \
&& pip3 install --no-cache-dir  --upgrade pip \
&& pip3 install --no-cache-dir -r requirements.txt
#RUN rm -rf /var/cache/apk

RUN chmod a+x /app/src/bin/run.sh
CMD [ "/app/src/bin/run.sh" ]

EXPOSE 22042
