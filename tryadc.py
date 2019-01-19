from Adafruit_ADS1x15 import ADS1x15
pga = 6144
sps = 8
adc = ADS1x15(ic=0x01)
adc.readADCSingleEnded(0, pga, sps)