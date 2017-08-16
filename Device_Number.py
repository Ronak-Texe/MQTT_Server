# Doing the bitwsie operation with integer is same as doing with hexadecimal
# This file is used for using a few individual bytes to combine them to form one single hexadecimal number

# This function combines the individual hexa decimal charactersticks
def HexCombine(bitmap,byte,shift_bit):
    temp_hexa=0x00000000 #The hexa decimal value is used for storing after the operations
    
    for i in range(byte): # Defines the length 
        temp_int=int(bitmap[i],16) #Converts to integer
        if(shift_bit>=0): # To make sure that the shift bit never goes below 8 as thats the maximum possible due to decrease of 8 everytime
            temp_hexa=((temp_int<<shift_bit) | temp_hexa) # Shifts the temp and then take the OR Sequence
            # temp_hexa |= (temp_int << shift_bit)
            #print(temp_hexa)
            shift_bit -= 8
    return(temp_hexa) # This calculated number is then used 
    
# Used to calcualte the device that has undergone change, Note: This does not tell when device is activated or deactivated
def CalcDeviceNum(bitmap,byte,shift_bit):
    device_number=[]
    temp_hexa=HexCombine(bitmap,byte,shift_bit) # Take the output from receiver and combine them to form one hexadecimal term
    for i in range(byte*8): # Byte is used to provide flexibility to ensure that 2/3/4 bytes of hexadecimal data can also be combined together. Not only restriced to 3 bytes of data
        if(temp_hexa & (1<<i)): # To determine which of these bits is 1 (active) by using the AND sequence. 
            device_number.append((i+1)) #
            
    if(device_number==[]): #If no device underwent change so it should store 0 and print that
        device_number=0
        
    return(device_number)
    


