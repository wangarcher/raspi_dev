import smbus
import socket
import RPi.GPIO as GPIO
from time import sleep
import serial

GPIO.setmode(GPIO.BCM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_master = "192.168.99.101"
port_battery_monitor = 10098

#bus1 = smbus.SMBus(1)
bus0 = smbus.SMBus(0)
t = 1

while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(17,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(22,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(27,GPIO.OUT,initial=GPIO.LOW)
    ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
    
    if (t % 4 == 1):
        try:   
            GPIO.output(4,GPIO.HIGH)
            sleep(0.3)
            sum1 = bus0.read_word_data(0x0b,0x09)     
            power1 = bus0.read_word_data(0x0b,0x0d)
            temp1 = bus0.read_word_data(0x0b,0x4a)
            amp1 = bus0.read_word_data(0x0b,0x0a)
            print(amp1)
            print(sum1)
            print(temp1)
            print(power1,"1")
            t = t + 1
            GPIO.output(4,GPIO.LOW)
            sleep(0.3)
        except IOError as e:
            print("null")
    if(t % 4 == 2):
        try:
            GPIO.output(17,GPIO.HIGH)
            sleep(0.3)
            sum2 = bus0.read_word_data(0x0b,0x09)
            power2 = bus0.read_word_data(0x0b,0x0d)
            temp2 = bus0.read_word_data(0x0b,0x4a)
            amp2 = bus0.read_word_data(0x0b,0x0a)
            print(sum2)
            print(temp2)
            print(power2,"2")
            t = t + 1
            GPIO.output(17,GPIO.LOW)
            sleep(0.3)
        except IOError as e:
            print("null")
    if(t % 4 == 3): 
        try:
            GPIO.output(27,GPIO.HIGH)
            sleep(0.3)
            sum3 = bus0.read_word_data(0x0b,0x09)
            power3 = bus0.read_word_data(0x0b,0x0d)
            temp3 = bus0.read_word_data(0x0b,0x4a)
            amp3 = bus0.read_word_data(0x0b,0x0a)
            print(sum3)
            print(temp3)
            print(power3,"3")
            t = t + 1
            GPIO.output(27,GPIO.LOW)
            sleep(0.3)
        except IOError as e:
            print("null")
    if(t % 4 == 0):
        try:
            GPIO.output(22,GPIO.HIGH)
            sleep(0.3)
            sum4 = bus0.read_word_data(0x0b,0x09)
            power4 = bus0.read_word_data(0x0b,0x0d)
            temp4 = bus0.read_word_data(0x0b,0x4a)
            amp4 = bus0.read_word_data(0x0b,0x0a)
            print(sum4)
            print(temp4)
            print(power4,"4")
            t = t + 1
            GPIO.output(22,GPIO.LOW)
            sleep(0.2)
            power = (power1+power2+power3+power4)/50 
            print(power)
            f = str(power)
            ser.write(f)
            
            sock.sendto(f.encode('utf-8'),(ip_master,port_battery_monitor))

        except IOError as e:
            print("null")
    GPIO.cleanup()
        

#        p = str(power1)
#        print(power1)
#        print(power2)
#        print(power3)
#        i = str(sum)
#        sock.sendto(p.encode('utf-8'),('192.168.1.110',10007))
#        sock.sendto(i.encode('utf-8'),('192.168.1.110',1 0007))
#if we have more time, we should advance the speed and stability of it. I am still doubting it      
