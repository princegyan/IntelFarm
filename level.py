

#--------------------------------------------------------------------------------------------------
#
#
#
#--------------------------------------------------------------------------------------------------
#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()

#GPIO SETUP
pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)
 
def callback(pin):
        if GPIO.input(pin):
                print ("Water Not Detected!")
        else:
                print ("Water Detected!")
def read_adc(self, channel, gain=1, data_rate=None):

 
#GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
#GPIO.add_event_callback(pin, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
while True:
        callback(pin)
        level = mcp3008.readadc(5)
        print "Moisture level: {:>5} ".format(level)
        time.sleep(5)

