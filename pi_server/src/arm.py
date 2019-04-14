import RPi.GPIO as GPIO
import time
import sys
import signal

out_vdd = 12
out_gnd = 11
max_duty = 65

GPIO.setmode(GPIO.BOARD)
GPIO.setup(out_vdd, GPIO.OUT)
GPIO.setup(out_gnd, GPIO.OUT)
vdd = GPIO.PWM(out_vdd, 100)
gnd = GPIO.PWM(out_gnd, 100)
gnd.start(0)
vdd.start(0)


def rotate_timed(t):
    vdd.ChamgeDutyCycle(max_duty)
    gnd.ChangeDutyCycle(0)
    time.sleep(t)
    vdd.ChangeDutyCycle(0)
    gnd.ChangeDutyCycle(0)
def start():
    vdd.ChangeDutyCycle(max_duty)
    gnd.ChangeDutyCycle(0)

def end():
    vdd.ChangeDutyCycle(0)
    gnd.ChangeDutyCycle(0)
