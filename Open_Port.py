##import serial
##
### What if the length of the string is not 7 more than  7 bytes. Should I cancel the pooling or
### shoudl I send you
### The request code of the device is defined by 'CODE+CRC(CODE)'
### For opening port it is 'C+CRC(C)'='0x43,0x01'
##def sendReceiver(request_code,number):
##    for i in range(1):
##        port = "COM4"
##        baud = 19200
##        
##        ser = serial.Serial(port, baud, timeout=1)
##        if ser.isOpen():
##            print("\n",ser.name + ' is open')
##        received_data=[]
##        #cmd = input("Enter any command to continue: ")
##        #bitmap=[0x43,0x01]
##        bits=bytearray(request_code)
##        ser.write(bits)
##    
##        count=0
##        for i in range(number): # Should I make it len. What if not 7 then wrong anyways?
##            for line in ser.read(): 
##                  #time.sleep(1)
##                 # print "line(" + str(count) + ")=" + line
##                  received_data.append(line)
##                  count=count+1
##                  #print(received_data[i] + "  and the "+hex(ord(received_data[i])))
##                  received_data[i]=hex((received_data[i]))
##                  #print(received_data[i] + "  and the "+bin(ord(received_data[i])))
##                  #print(received_data)
##    return(received_data)
##    ser.close()
##    
