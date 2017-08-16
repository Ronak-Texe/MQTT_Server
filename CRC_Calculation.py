# Determine the CRC and compare it. This is done to check for if the information received by the computer
# is what what it asked for in the beginning.

def UpdateCRC8(crc,data): # Calcualtes the CRC starting with the request character 'C/S/I' and the data received
    crc^=data  # XOR taken with the CRC of request code and the data received
    for i in range(8):# This loop runs 8 times as each byte has 8 bits. It does not mean that it accesses each bit. It just shifts the data till 8 times
        
    # This algorithm/concept is pre-defined and so no explanantion for the methodology
        if(crc & 0x80):# This incvolves taking the  AND of CRC and 1000 0000
            crc=(crc<<1)^(0x85)#This step involves shifting each bit by 1 
           # print(crc)
            #print("\nYou have reached here\n")
        else:
            crc=crc<<1 
    return (crc)
    
def CalcRC8(data,byte):# This is the main function which calls the other function that calcualtes the CRC
    crc=0xff# CRC calculation always start with the maximum number 1111 1111
    for i in range(byte): # This loops depending on the number of data provided and then calculates CRC
        crc=UpdateCRC8(crc,data[i]) #The CRC value always changes as is the used an input
    return(hex(crc & 0xff))# Masking of data to make sure that it remains within the 32 bit number

def CompareCRC(initial_data, final_crc): # Compares the CRC obtained above with the final character of the totol data received which is the CRC as well
    if(int(initial_data,16)==int(final_crc,16)):
        print("CRC Matched")
    else:
        print("CRC Fail to Match")