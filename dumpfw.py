from serial import * 
#get handler
ser = Serial("/dev/tty.usbserial", 9600, timeout=1,parity=PARITY_EVEN)

def cmd_get(hser):
    hser.write("\x00\xff")
    data = hser.read(15)
    print data.encode("hex") 

def cmd_verproc(hser):
    hser.write("\x01\xfe")
    data = hser.read(15)
    print data.encode("hex") 
        
def cmd_getid(hser):
    hser.write("\x02\xfd")
    data = hser.read(15)
    print data.encode("hex") 

def cmd_readmem(hser,address):
    hser.write("\x11\xee")
    data = hser.read(1)
    print data.encode("hex") 

def cmd_writemem(hser):
    hser.write("\x31\xce")
    data = hser.read(1)
    print data.encode("hex") 

def cmd_erasemem(hser):
    hser.write("\x43\xbc")
    data = hser.read(1)
    print data.encode("hex") 

def cmd_extendederasemem(hser):
    hser.write("\x44\xbb")
    data = hser.read(1)
    print data.encode("hex") 

def cmd_writeunprotect(hser):
    hser.write("\x73\x8c")
    data = hser.read(1)
    print data.encode("hex") 

try:
    ser.write("\x7f") #enter bootloader
    resp = ser.read()
    if(resp != "\x79"):
        raise SerialException
    cmd_get(ser) 
    cmd_verproc(ser)  
    #cmd_getid(ser)
    #cmd_readmem(ser,0x0000)
    #cmd_writemem(ser)
    #cmd_extendederasemem(ser)
    cmd_writeunprotect(ser)
 
except SerialException:
    print "something happened?"

#def cmd_ 

