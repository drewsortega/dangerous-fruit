import RPi.GPIO as GPIO
import time 

out1 = 29
out2 = 31
out3 = 33
out4 = 32

i=0
positive=0
negative=0
y=0



GPIO.setmode(GPIO.BOARD)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)
GPIO.output(out1,GPIO.LOW)
GPIO.output(out2,GPIO.LOW)
GPIO.output(out3,GPIO.LOW)
GPIO.output(out4,GPIO.LOW)

def spin(t, o1, v1, o2, v2):
    GPIO.output(o1,v1)
    GPIO.output(o2,v2)
    time.sleep(t)
    GPIO.output(o1,GPIO.LOW)
    GPIO.output(o2,GPIO.LOW)

def left_forward(t):
    spin(t, out3, GPIO.HIGH, out4, GPIO.LOW)

def left_backward(t):
    spin(t, out3, GPIO.LOW, out4, GPIO.HIGH)

def right_forward(t):
    spin(t, out1, GPIO.LOW, out2, GPIO.HIGH)


def right_backward(t):
    spin(t, out1, GPIO.HIGH, out2, GPIO.LOW)


def forward(t):
    GPIO.output(out1,GPIO.LOW)
    GPIO.output(out2,GPIO.HIGH)
    GPIO.output(out3,GPIO.HIGH)
    GPIO.output(out4,GPIO.LOW)
    time.sleep(t)
    GPIO.output(out1,GPIO.LOW)
    GPIO.output(out2,GPIO.LOW)
    GPIO.output(out3,GPIO.LOW)
    GPIO.output(out4,GPIO.LOW)



def backward(t):
    GPIO.output(out1,GPIO.HIGH)
    GPIO.output(out2,GPIO.LOW)
    GPIO.output(out3,GPIO.LOW)
    GPIO.output(out4,GPIO.HIGH)
    time.sleep(t)
    GPIO.output(out1,GPIO.LOW)
    GPIO.output(out2,GPIO.LOW)
    GPIO.output(out3,GPIO.LOW)
    GPIO.output(out4,GPIO.LOW)


def left(t):
    GPIO.output(out1,GPIO.HIGH)
    GPIO.output(out2,GPIO.LOW)
    GPIO.output(out3,GPIO.HIGH)
    GPIO.output(out4,GPIO.LOW)
    time.sleep(t)
    GPIO.output(out1,GPIO.LOW)
    GPIO.output(out2,GPIO.LOW)
    GPIO.output(out3,GPIO.LOW)
    GPIO.output(out4,GPIO.LOW)



def right(t):
    GPIO.output(out1,GPIO.LOW)
    GPIO.output(out2,GPIO.HIGH)
    GPIO.output(out3,GPIO.LOW)
    GPIO.output(out4,GPIO.HIGH)
    time.sleep(t)
    GPIO.output(out1,GPIO.LOW)
    GPIO.output(out2,GPIO.LOW)
    GPIO.output(out3,GPIO.LOW)
    GPIO.output(out4,GPIO.LOW)

def cleanup():
    GPIO.output(out1,GPIO.LOW)
    GPIO.output(out2,GPIO.HIGH)
    GPIO.output(out3,GPIO.LOW)
    GPIO.output(out4,GPIO.HIGH)
    GPIO.cleanup()
            
