#!/usr/bin/env python

# import asyncio
from threading import Timer
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time as time
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
import argparse
from NoSimpleMFRC522 import NoSimpleMFRC522

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text
from luma.core.legacy.font import proportional, LCD_FONT

def demo(letter, message):
    global device, text, canvas, proportional, LCD_FONT, lcd
    with canvas(device) as draw:
        #draw.rectangle(device.bounding_box, outline="white")
        text(draw, (0, 0), letter, fill="white", font=proportional(LCD_FONT))
    lcd.text(message, 0)
    time.sleep(2)
    device.clear()
    lcd.clear()
    return 0

if __name__ == "__main__":
    reader = SimpleMFRC522()
    lcd = LCD()

    serial = spi(port=1, device=2, gpio=noop())
    device = max7219(serial, width=8, height=8, rotate=0, block_orientation=0)

    GPIO.setup(33,GPIO.OUT,initial=0)
    GPIO.setup(37,GPIO.OUT,initial=0)

    correct = ['ok']

    # GPIO.setmode(GPIO.BCM)

    def led(pin,sec):
        GPIO.output(pin, GPIO.HIGH)
        if pin == 33:
            run = Timer(0, demo, ("Y", "Valid card"))
        else:
            run = Timer(0, demo, ("N", "Invalid card"))
        run.start()
        time.sleep(sec)
        GPIO.output(pin, GPIO.LOW)

    try:
        while True:
            # try:
            id, code = reader.read()
            print(id)
            print('"',code,'"')
            if code.strip() == 'ok':
                led(33,1)
            else:
                led(37,1)
            # except Exception as e:
            #     print(e)
    except KeyboardInterrupt:
        print('Bye')
        pass
    finally:
        GPIO.cleanup()
