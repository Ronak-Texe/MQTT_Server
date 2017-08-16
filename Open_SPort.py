import serial
import time
 
port = "COM4"
baud = 19200
payload_data=[]
while True:
    received_data=[]
    ser = serial.Serial(port, baud, timeout=1)
    if ser.isOpen():
        print(ser.name + ' is open...')
    cmd = raw_input("Enter command or 'exit':")
    bitmap=[0x43,1]
    bits=bytearray(bitmap)
    ser.write(bits)

    count=0
    for i in range(7):
        for line in ser.read(): 
              time.sleep(1)
             # print "line(" + str(count) + ")=" + line
              received_data.append(line)
              count=count+1
              #print(received_data[i] + "  and the "+hex(ord(received_data[i])))
              received_data[i]=hex(ord(received_data[i]))
              #print(received_data[i] + "  and the "+bin(ord(received_data[i])))
              #print(received_data[i])#
              
      
    for i in range(1,5):
        payload_data.append(received_data[i])
    print(payload_data)
    ser.close()

            