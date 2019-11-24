#!/usr/bin/env sh
CONFIG_PATH=/data/options.json

export MQTT_BROKER_IP="$(jq --raw-output '.mqttBrokerServer' $CONFIG_PATH)"
export MQTT_BROKER_PORT="$(jq --raw-output '.mqttBrokerPort' $CONFIG_PATH)"
export MQTT_USER="$(jq --raw-output '.mqttUser' $CONFIG_PATH)"
export MQTT_PASSWORD="$(jq --raw-output '.mqttPassword' $CONFIG_PATH)"
export KEEPALIVE="$(jq --raw-output '.keepAlive' $CONFIG_PATH)"

/app/src/bin/tHome-eagle.py -c /app/src/conf