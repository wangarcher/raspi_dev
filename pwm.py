import RPi.GPIO as GPIO
from time import sleep

def my_callback(channel):
    global ledState
    global s
    if channel==24:
        ledState = not ledState
        s=s+2

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
p=GPIO.PWM(25,50)
p.start(0)
GPIO.add_event_detect(24,GPIO.RISING,callback=my_callback,bouncetime=200)

ledState=GPIO.LOW
s=0
try:
    while True:
        duty = s
        p.ChangeDutyCycle(duty)
        sleep(0.02)

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
