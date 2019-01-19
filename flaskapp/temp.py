
import smbus
import time


counter = 1
while(counter ==1 ):
	bus = smbus.SMBus(1)
	bus.write_byte(0x40, 0xF3)

	time.sleep(0.3)
	data0 = bus.read_byte(0x40)
	data1 = bus.read_byte(0x40)

	cels = ((data0 * 256 + data1) * 175.72 / 65536.0)-46.85

	print('Atmospheric Temperature is %.2fc' % (cels))
	time.sleep(2)

