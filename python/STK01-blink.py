#!/usr/bin/python
import onionGpio
import time

print "STK01-blink.py started"

sleepTime = 0.5
# create a GPIO object
gpio0 = onionGpio.OnionGpio(0)
# set the output direction with zero(LOW) being the default value
gpio0.setOutputDirection(0)
ledValue = 1
while 1:
	gpio0.setValue(ledValue)
	if ledValue == 1:
		ledValue = 0
	else:
		ledValue = 1
	time.sleep(sleepTime)


print "STK01-blink.py ended"


