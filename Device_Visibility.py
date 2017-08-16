import Open_Port
import Device_Number
#import numpy

def DeviceVisibility(number_of_devices): # The argument can be a call as of teh length of the device_number variable in the Control Panel Class
    # Do I need to check for repeating values as that would take a lot of time a n
    #device_visibility=numpy.zeros((number_of_devices,2))
    file=open('Commission Mode Data.txt','w')
    file.write('Device Numer\t\tVisible Devices\n')
    #i=0
    device_visibility=[]

    #while((device_visibility[number_of_devices-1][0])==0.0):
    while(len(device_visibility)!=number_of_devices*2):
        master_information=Open_Port.sendReceiver([0x59,0xde],19)
        device_number=int(master_information[13],16)
        request_information=[master_information[14],master_information[15],master_information[16],master_information[17]]
        #print('\n\n',request_information)
        visibility=Device_Number.CalcDeviceNum(request_information,len(request_information),24)
        #print('\n\n',visibility,'\n\n')
        
#        if device_number!=0:
#            print('\n\nI AM HERE!!!!\n\n')
#            device_visibility[i][0]=device_number
#            device_visibility[i][1]=visibility
#            i+=1
        if device_number!=0:
            device_visibility.append(device_number)
            device_visibility.append(visibility)
            file.write('{:5} {:>30}\n'.format(str(device_number),str(visibility)))

#    for i in range(number_of_devices*2-1):  
#        print(device_visibility[i],'  ',device_visibility[i+1],'\n')
        
        
    