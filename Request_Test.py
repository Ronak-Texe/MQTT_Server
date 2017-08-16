import Open_Port
import Device_Number
import CRC_Calculation
import time
import requests


payload_data=[]
deviceNumber_data=[]
request_code=[]

received_data=Open_Port.sendReceiver([0x43,0x01],7)



for i in range(6):# Received data is of 7 bytes and the 1st byte is always the CRC of 'C/F/'
    payload_data.append(int(received_data[i],16))
    if(i>0 and i<5):# Store the bytes from 1-4 as they contain the useful data
        deviceNumber_data.append(received_data[i])

device_number=Device_Number.CalcDeviceNum(deviceNumber_data,len(deviceNumber_data),24)


for i in range(len(device_number)):
    CRC=(CRC_Calculation.CalcRC8([0x49,device_number[i]],2))
    request_code.append([0x49,device_number[i],int(CRC,16)])
    #print(request_code)
print('\nWaiting')
time.sleep(2)


data_sensor=[]
for i in range(len(device_number)):
    data_sensor.append(str(Open_Port.sendReceiver(request_code[i],27)))

r=requests.post('http://127.0.0.1/upload',data=str(received_data))
print(r.status_code,r.reason)

r=requests.post('http://127.0.0.1/upload2',data=str(data_sensor))
print(r.status_code,r.reason)


