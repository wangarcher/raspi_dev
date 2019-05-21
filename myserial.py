import serial, time
import numpy as np
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(32, GPIO.OUT)
#p = GPIO.PWM(32, 50)  

def str2float(s):
    try:
        return float(s)
    except ValueError:
        return 0

def serialChecker(autoChoice=True, *devType): # autoChoice : find first accessible one
	import os
	DEV_PATH="/dev/"
	if devType==():
		devType=["ttyUSB", "ttyAMA", "ttyACM", "rfcomm"]
	else :
		devType = list(devType)
		for i in range(len(devType)):
			if devType[i].isupper():
				devType[i] = "tty" + devType[i]

	#order changes:
	devFilter=' '.join([DEV_PATH+t+'*' for t in devType])
	devs=os.popen('ls '+devFilter).read().split()
	
	devs=[]
	for t in devType:
		devs += os.popen('ls ' + DEV_PATH+t+'* 2> /dev/null').read().split()

	if devs==[]: raise IOError(2,"No avaliable device.")

	if autoChoice:
		for d in devs:
			if os.access(d,os.R_OK|os.W_OK):
				return devs   #modified to return all

	for d in devs:
		print("Permission for "+d+" ?")
		if os.access('/usr/bin/kdesudo',os.X_OK):
			os.popen('kdesudo chmod 666 '+d)
		elif os.access('/usr/bin/kdesu',os.X_OK):
			os.popen('kdesu chmod 666 '+d)
		elif os.access('/usr/bin/gksudo',os.X_OK):
			os.popen('gksudo chmod 666 '+d)

		if os.access(d,os.R_OK|os.W_OK):
			return d

	raise IOError(13,"All devices' permissions denied.")
	return None
    
dev = serialChecker(True, 'ACM') #For *unix
print(dev)
ser = serial.Serial(dev[0], 9600, timeout = 0.0001)
#tombed = serial.Serial(dev[1], 115200, timeout = 0.0001)

#p.start(0)

while True:
    try:
        ser.write('?')
    
        s = ser.readline()
        rct_ngl = str2float(s)/100      # arccosvalue
        rdn = np.arccos(rct_ngl)        # transform to radian
        dgr = (rdn * 180 / np.pi) - 90
        print(dgr)
        #ctl = (dgr*9.5/180)+2.5
        #ctl = round(ctl,2)

        #p.ChangeDutyCycle(ctl)
        #print(ctl)
        #time.sleep(0.01)
        # mode abcde
        #if (dgr <-40):
        #    tombed.write("a")
        #elif (dgr < -30) and (dgr > -40):
        #   tombed.write("b")
        #elif (dgr < -20) and (dgr > -30):
        #    tombed.write("c")
        #elif (dgr < -10) and (dgr > -20):
        #    tombed.write("d")
        #elif (dgr < 0) and (dgr > -10):
        #    tombed.write("e")
           
    except KeyboardInterrupt:

        #tombed.write("x")
        print("motion start")
        #p.stop()
        #GPIO.cleanup()
   

