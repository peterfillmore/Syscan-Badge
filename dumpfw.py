import serial
#get handler
ser = serial.Serial("/dev/tty.usbserial", 9600, timeout=1,parity=serial.PARITY_EVEN)

try:
    ser.write("\x7f") #enter bootloader
    if(ser.read() != "y"):
        raise exception serial.SerialException

except exception serial.SerialException:
    print "something happened?"

def cmd_get(hser):
    hser.write("\x00\xff")
    hser.read()
 

