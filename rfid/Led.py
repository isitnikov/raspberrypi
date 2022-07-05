#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)

print("Green LED on")

GPIO.output(21,GPIO.HIGH)

time.sleep(5)

print("Green LED off")

GPIO.output(21,GPIO.LOW)

print("Red LED on")

GPIO.output(20,GPIO.HIGH)

time.sleep(5)

print("Red LED off")

GPIO.output(20,GPIO.LOW)
