import CRC_Calculation
import Open_Port
import Device_Number
import Device_Status
import Signal_Strength
import time

def SensorInformation(device_number,data_sensor):
    request_code=[]
    file = open("Sensor Data.txt","w") # Creating the file
    file.write('Device Number\tDevice Type\tTime of Request\tTemperature\tDevice Alert\t\tDevice Status\tDevice Path\tRoute Signal Strength\t Last Polled (mins ago)\n')
    
#    if len(device_number)!=0:
#        for i in range(len(device_number)):
#            CRC=(CRC_Calculation.CalcRC8([0x49,device_number[i]],2))
#            request_code.append([0x49,device_number[i],int(CRC,16)])
#            #print(request_code)
#        
#        print('\nWaiting')
#        time.sleep(2)
    if device_number!=0:
        for i in range(len(device_number)):
                #data_sensor=Open_Port.sendReceiver(request_code[i],27)
                temp_time=time.localtime()
                device_alert=data_sensor[i][15]
                device_status=data_sensor[i][14]
                device_polling=(40-int(data_sensor[i][13],16))/2
                #device_path=[int(data_sensor[8],16),int(data_sensor[9],16)]
                #print(device_status,'\t',i)
                temperature_sensor=int(data_sensor[i][16],16)
                serial_number=data_sensor[i][2]
                #print("Serial Number is",hex(serial_number))
                if(int(device_alert,16)==0x01):
                    print("\nDevice ", device_number[i], " is ACTIVATED!!")
                    status_sensor='ACTIVATED'
                else:
                    print("\nDevice ", device_number[i], " is DEACTIVED")
                    status_sensor='DEACTIVATED'
                    
                status=Device_Status.DeviceStatus(device_status)
                
                print("Temperature of Device ",device_number[i], " is ",temperature_sensor,' degrees\n')
                print("Current Time:",temp_time[3],':',temp_time[4])
            
                print('Device Status: ',status)
                print('Device Path: ',device_number[i],'-',int(data_sensor[i][8],16),'-',int(data_sensor[i][9],16),'\n')
                device_signal=Signal_Strength.SignalStrength([data_sensor[i][10],data_sensor[i][11],data_sensor[i][12]])
                print("Device Signal: ",device_signal)
         
                if(serial_number=='0x21'):
                    print("Device Type: Contact Sensor")
                    device_type='Contact Sensor'
                elif(serial_number=='0x14' or serial_number=='0x11' or serial_number=='0x16'):
                    print("Device Type: PIR Sensor")
                    device_type='PIR Sensor'
                else:
                    device_type='Unknown'
                    #WHY WOULD YOU NEED TO LOG TIME? HOW IN REAL LIFE USEFUL
                #file.write(str(device_number[i])+'\t\t'+device_type+'\t\t'+str(temp_time[3])+':'+str(temp_time[4])+'\t\t'+str(temperature_sensor)+'\t'+status_sensor+'\t'+str(status)+'\t '+str(device_number[i])+'-'+str(int(data_sensor[8],16))+'-'+str(int(data_sensor[9],16))+'\t\t'+str(device_signal[0])+'/'+str(device_signal[1])+'/'+str(device_signal[2])+'\t\t'+str(device_polling)+'\n')
                #file.write('{:20s} {:40s}  {:20s}\n'.format(device_type,str(status),str(temp_time[3])))
                file.write(' {:5} {:>20} {:>10}{}{} {:>10} {:>22} {:>25} {:>8}{}{}{}{} {:>13}{}{}{}{} {:>20} \n'.format(str(device_number[i]),device_type,str(temp_time[3]),':',str(temp_time[4]),str(temperature_sensor),status_sensor,str(status),str(device_number[i]),'-',(int(data_sensor[i][8],16)),'-',str(int(data_sensor[i][9],16)),str(device_signal[0]),',',str(device_signal[1]),',',str(device_signal[2]),str(device_polling)))
    else:
        print("No Device is activated yet")
    file.close()
