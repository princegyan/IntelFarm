'''
	Dennis Effa Amponsah
	Prince Alfred Gyan
'''
import smbus           #
from time import sleep
from soiltemp import sensor, loop, kill  #import the soiltemp file

serialNum = sensor()  #take a look in the soil temp file for clarrification
counter=1   


while(counter == 1):
	bus = smbus.SMBus(1)
	bus2 =smbus.SMBus(1)
	bus.write_byte(0x40, 0xF3)    #sets the address to write data to and sets the mode to No Hold master mode
	bus2.write_byte(0x76, 0xF5)	#sets the mode to no hold master mode

	sleep(0.3)  #sleep for sometime for setup

	data0 = bus.read_byte(0x40)   
	data1 = bus.read_byte(0x40)
	humidd0 = bus2.read_byte(0x40)
	humidd1 = bus2.read_byte(0x40)

	cels = ((data0 * 256 + data1) * 175.72 / 65536.0)-46.85   #conversion for celcius
	humidity = ((humidd0 * 256 + humidd1)*125 / 65536.0)-6		#conversion for humidity

        print('Temperature is %.2fc' % (cels))
        print('Humidity is %.2f%%' % (humidity))
	loop(serialNum)   #called from the soil temp file
        sleep(2)

