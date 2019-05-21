import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
p=GPIO.PWM(25,50)
p.start(0)

s=3
try:
    while True:
        if GPIO.input(24)==GPIO.HIGH:
            s=s+3
            duty = s
            p.ChangeDutyCycle(duty)
            sleep(0.1)# stupid
            
except KeyboardInterrupt:
    pass
GPIO.cleanup()

