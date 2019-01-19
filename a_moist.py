import Adafruit_ADS1x15

import time

adc = Adafruit_ADS1x15.ADS1115()

gain = 1

while True:
    value = adc.read_adc(0,gain)
    print'Value is: ', value
    time.sleep(0.5)
