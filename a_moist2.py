import Adafruit_ADS1x15

from time import sleep

adc = Adafruit_ADS1x15.ADS1115()

while True:
    print 'Value : ', adc.read_adc(0, 1)
    sleep(1)
    #print 'Converted value : ', adc.start_adc(0, 1)