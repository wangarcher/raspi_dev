import serial, time
import numpy as np
ser = serial.Serial("/dev/ttyACM1", 9600, timeout = 0.0001)

def str2float(s):
    try:
        return float(s)
    except ValueError:
        return 0
    
while True:
    
    ser.write('?')
    #time.sleep(0.01)
    s = ser.readline()
    rct_ngl = str2float(s)/100      # arccosvalue
    rdn = np.arccos(rct_ngl)        # transform to radian
    dgr = (rdn * 180 / np.pi) - 90
    print s


    

