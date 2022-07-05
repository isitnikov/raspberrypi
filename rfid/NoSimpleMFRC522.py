# Code by Simon Monk https://github.com/simonmonk/

from mfrc522 import SimpleMFRC522
from mfrc522 import MFRC522
import RPi.GPIO as GPIO

class NoSimpleMFRC522(SimpleMFRC522):
    def __init__(self):
        self.READER = MFRC522(device=0,pin_rst=16)
