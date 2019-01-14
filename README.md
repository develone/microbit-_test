# 01/12/19
# Goal: To add Bluethooth to the RPi with a FPGA
I just was able to get the first Ultibo example working on the microbit & bare metal
RPi3B  https://github.com/develone/microbit-_test/blob/master/first_ex_mark/pic/a.jpeg
& https://github.com/develone/microbit-_test/blob/master/first_ex_mark/pic/b.jpeg
When you press the buttons on the microbit it displays A or B sends the indication on
The RPi3B.  Microbit 16 MHz 32-bit ARM Cortex-M0 microcontroller, 256 KB flash memory, 
16 KB static ram, 2.4 GHz Bluetooth, Accelerometer, Magnetometer, 25 LEDs in a 5×5 array,
Three tactile pushbuttons (two for user, one for reset).  
The micro bit can be program from cell phone using the Bluetooth.  I have been able to 
test the example find my phone which when y press a Button Use the phone to tell you here I am.

On power up and reset the micro displays "ULTIBO 98".
Only 8 files are needed on the micro sd to boot on all version of the RPi
RPi Zero, RPi, RPi2B, RPi3B and RPi3B+
## bootcode.bin
## fixup.dat  
## start.elf
## kernel=microbitdemo-kernel-RPI.img
## kernel=microbitdemo-kernel-RPI2.img
## kernel=microbitdemo-kernel-RPI3.img
## microbitdemo-cmdline.txt
## microbitdemo-config.txt
