
def SignalStrength(signal):
    dB_signal=[]
    for i in range(len(signal)):
        int_signal=int(signal[i],16)
        if(int_signal>=128):
            dB_signal.append((int_signal-256)/2 - 74)
        elif(int_signal<128):
            dB_signal.append((int_signal)/2 - 74)
        if(int_signal==0):
            dB_signal[i]=None
    return(dB_signal)
