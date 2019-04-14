import RPi.GPIO as GPIO
import time
import sys
import signal

out_vdd = 12
out_gnd = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(out_vdd, GPIO.OUT)
GPIO.setup(out_gnd, GPIO.OUT)
GPIO.output(out_vdd, GPIO.LOW)
GPIO.output(out_gnd, GPIO.LOW)

def rotate_timed(t):
    GPIO.output(out_vdd, GPIO.HIGH)
    GPIO.output(out_gnd, GPIO.LOW)
    time.sleep(t)
    GPIO.output(out_vdd, GPIO.LOW)
    GPIO.output(out_gnd, GPIO.LOW)

def start():
    GPIO.output(out_vdd, GPIO.HIGH)
    GPIO.output(out_gnd, GPIO.LOW)

def end():
    GPIO.output(out_vdd, GPIO.LOW)
    GPIO.output(out_gnd, GPIO.LOW)
