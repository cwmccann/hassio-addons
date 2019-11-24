#===========================================================================
#
# Port to use for the web server.  Configure the Eagle to use this
# port as it's 'cloud provider' using http://host:PORT
#
#===========================================================================
httpPort = 22042

#===========================================================================
#
# MQTT topic names
#
#===========================================================================
# Meter reading topic (reports current meter reading in kWh)
mqttEnergy = 'power/elec/Home/energy'

# Instantaneous power usage topic (reports power usage in W)
mqttPower = 'power/elec/Home/power'

#Current price topic (returns current price of electricity from meter)
mqttPrice = 'power/elec/Home/price'

#Current rate label (returns rate label from meter)
mqttRateLabel = 'power/elec/Home/ratelabel'

#===========================================================================
#
# Logging configuration.  Env variables are allowed in the file name.
#
#===========================================================================
logFile = 'stdout'
logLevel = 20

