import RPi.GPIO as GPIO
import time 

out1 = 29
out2 = 31
out3 = 33
out4 = 32



GPIO.setmode(GPIO.BOARD)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)
o1 = GPIO.PWM(out1, 100)
o2 = GPIO.PWM(out2, 100)
o3 = GPIO.PWM(out3, 100)
o4 = GPIO.PWM(out4, 100)
o1.start(0)
o2.start(0)
o3.start(0)
o4.start(0)

max_duty = 50

def forward(t):
    o1.ChangeDutyCycle(0)
    o2.ChangeDutyCycle(max_duty)
    o3.ChangeDutyCycle(max_duty)
    o4.ChangedutyCycle(0)
    time.sleep(t)
    o1.ChangeDutyCycle(0)
    o2.ChangeDutyCycle(0)
    o3.ChangeDutyCycle(0)
    o4.ChangeDutyCycle(0)


def backward(t):
    o1.ChangeDutyCycle(max_duty)
    o2.ChangeDutyCycle(0)
    o3.ChangeDutyCycle(0)
    o4.ChangedutyCycle(max_duty)
    time.sleep(t)
    o1.ChangeDutyCycle(0)
    o2.ChangeDutyCycle(0)
    o3.ChangeDutyCycle(0)
    o4.ChangeDutyCycle(0)
