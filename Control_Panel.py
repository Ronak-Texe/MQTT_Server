# The Main file that controls and calling of other functions. This imports all other files. 
import CRC_Calculation #  File names
import Device_Number
#import Open_Port
import ast
#import Device_Status
#import Signal_Strength
import Sensor_Information
#import Http_Server
#import http.server
import time
    

def ControlPanel1(Data):
    file = open("Sensor Data.txt","w") # Creating the file
    file.write('Device Number\tDevice Type\tTime of Request\tTemperature\tDevice Alert\tDevice Status\tDevice Path\tRoute Signal Strength\n')
    global device_number
    received_data=ast.literal_eval(Data)
    
    payload_data=[]
    deviceNumber_data=[]
     
    for i in range(6):# Received data is of 7 bytes and the 1st byte is always the CRC of 'C/F/'
        payload_data.append(int(received_data[i],16))
        if(i>0 and i<5):# Store the bytes from 1-4 as they contain the useful data
            deviceNumber_data.append(received_data[i])
    
    print("\nWaiting....\n")
    time.sleep(2)
    
    CRC_Output=CRC_Calculation.CalcRC8(payload_data,len(payload_data)) # Calling CRC to calculate 
    CRC_Calculation.CompareCRC(CRC_Output,received_data[6])     # and match the CRC code
    
    device_number=Device_Number.CalcDeviceNum(deviceNumber_data,len(deviceNumber_data),24)# Calculates the Device that underwent change, using the argument of data which was calculated earlier
    print("\nWaiting....\n")
    time.sleep(2)
    print("The device that underwent changes are as follows")
    print(device_number)
    
    
def ControlPanel2(Data2):
    
    sensor_data=ast.literal_eval(Data2)
    
    for i in range(len(device_number)):
        sensor_data[i]=ast.literal_eval(sensor_data[i])

    Sensor_Information.SensorInformation(device_number,sensor_data)# Calculates the staus, temperature and other information regarding every sensor and sto
