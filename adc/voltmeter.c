/* pcf8591.c Reads out the pcf8591 8 bit ADC and writes values to the DAC
 *    Copyright U. Raich Jan. 2017
 *    This program is part of a course on embedded systems held
 *    at the University of Cape Coast, Ghana in 2017
 *    It is released under the GNU Public License 
 *    For details please see https://www.gnu.org/licenses/gpl.html
 */
#include <stdio.h>
#include <pigpiod_if2.h>
#include <unistd.h>
#include <stdbool.h>
#include <hd44780.h>

#define I2C_BUS          1
#define I2C_FLAGS        0
#define PCF8591_ADDRESS  0x48
#define Vcc              3.3

bool pcf8951Debug = false;

void pcf8591SetDebug(bool onOff) {
  pcf8951Debug=onOff;
}

int main(int argc, char **argv) {
  static  int retCode;
  static  int pi,handle;
  int i,j;
  unsigned char value[4], controlByte, dacValue;
  char text[17]={'\0'};
  float resolution, fvalue;
  pcf8591SetDebug(true);
  hd44780SetDebug(false);
  
  /*
    set debugging on
  */

  if ((retCode = hd44780Open()) < 0) {
    printf("pcf8951: Cannot initialize pigpio\n");
    return -1;
  }

  if (hd44780PutS("Voltmeter:") < 0)
    printf("pcf8951: Writing Hello World failed!\n");
 
  if ((retCode == pigpio_start(NULL,NULL)) < 0) {
    printf("pcf8591: Cannot initialize pigpio\n");
    return -1;
  }
  else
    pi=retCode;  
  if (pcf8951Debug)
    printf("pcf8951: pigpio successfully initialized\n");

  if ((retCode = i2c_open(pi,I2C_BUS,PCF8591_ADDRESS,I2C_FLAGS)) < 0) {
    printf("pcf8951: Cannot open I2C bus %d at address %02x\n",
	   I2C_BUS,PCF8591_ADDRESS);
    if ((pigifError_t)retCode == pigif_bad_send) {
      printf("Did you start the pigpiod daemon?\n");
      return -1;
    }
  }
  handle = retCode;
  if (pcf8951Debug) {
    printf("pcf8951: I2C bus %d successfully opened on address %02x\n",
	   I2C_BUS,PCF8591_ADDRESS);
    printf("handle = %d\n",handle);
  }
  
  controlByte= 0x44;
  retCode = i2c_write_byte(pi, handle, controlByte);
  if (retCode < 0) {
    printf("pcf8951; Cannot write control byte 0x%02x to address 0x%02x\n",
	   controlByte,PCF8591_ADDRESS);
    return -1;
  }

  resolution = Vcc/256.0;
  for (i=0;i<100;i++) {
    /*
      every 4 secs write a new value to the DAC
    */
    if (!(i%4)) {
      dacValue = (unsigned char) (i&0xff)<<3;
      printf("pcf8951: write 0x%02x to DAC\n",dacValue);
      retCode=i2c_write_byte_data(pi,handle,controlByte,dacValue);
      if (retCode < 0) {
	printf("pcf8951: Cannot write DAC \n");
	return -1;	
      }
    }      
    for (j=0;j<4;j++) {
      retCode = i2c_read_byte(pi, handle);
      if (retCode < 0) {
	printf("pcf8951; Cannot read from address 0x%02x\n",
	      PCF8591_ADDRESS); 
	return -1;
      }
      else
	value[j]=retCode & 0xff;
    }    
    printf("%02x %02x %02x %02x\n",value[0],value[1],value[2],value[3]);
    /*
      send the values to the LCD display
    */
    hd44780SecondLine();
    fvalue = value[0]*resolution;
    sprintf(text,"0x%02x  <=> %4.2fV",value[0],fvalue);
    printf("Result: %s\n",text);
    if (hd44780PutS(text) < 0)
    printf("pcf8951: Writing result values failed!\n");
    sleep(1);
  }

  hd44780Close();    
  i2c_close(pi,handle);
  pigpio_stop(pi);
  return 0;
}
