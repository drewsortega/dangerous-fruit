import RPi.GPIO as GPIO
import time
import sys

out_vdd = 12
out_gnd = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(out_vdd, GPIO.OUT)
GPIO.setup(out_gnd, GPIO.OUT)
GPIO.output(out_vdd, GPIO.LOW)
GPIO.output(out_gnd, GPIO.LOW)
try:
    while(1):
        GPIO.output(out_vdd, GPIO.HIGH)
        GPIO.output(out_gnd, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.output(out_vdd, GPIO.LOW)
    GPIO.output(out_gnd, GPIO.LOW)
    GPIO.cleanup()
