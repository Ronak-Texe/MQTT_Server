# This file gets the status of the device based on the status byte  which is one of the bytes received by the computer with 'I' command

def DeviceStatus(status):
    device_status=[]
    for i in range(8): # Because maximum 8 possible combinations possible. Read the Ricochet document for 'modes'. Nothing to do with bits
        if(int(status,16) & (1<<i)):# Each time the loop runs, it runs through each and ever bit of the 'status' which is 1byte=8 bits, to check if any of the bits are 1 
            if(i==0):       #As the status of device depends which bit is high and so that's why loop through each bit and shifts the 1 left every time by 1/2/3/4/5.. until 8
                device_status.append('Front Tamper')
            if(i==1):
                device_status.append('Rear Tamper')
            if(i==2):
                device_status.append('Mask')
            if(i==3):
                device_status.append('Device Fault')
            if(i==4):
                device_status.append('Power Failure')
                
        if(device_status==[]): 
            device_status.append('Normal')
            
    return(device_status)
    