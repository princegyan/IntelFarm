import smbus
import time

counter =1
while(counter == 1):
	bus = smbus.SMBus(1)
	bus.write_byte(0x40, 0xE5)

	time.sleep(0.3)

	data0 = bus.read_byte(0x40)
	data1 = bus.read_byte(0x40)

	humidity = ((data0 * 256 + data1)*125 / 65536.0)-6

	time.sleep(0.3)

	print('Humidity is %.2f%%'% (humidity))

while(counter ==1):
	print('Humidity is %.2f%%' % (humidity))
	time.sleep(2)
