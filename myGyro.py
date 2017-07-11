import serial
import matplotlib.pyplot as plt
import sys
from PyQt5.Qt import *

class ArduinoSerial:
    boudrate = 9600
    com_port = 'COM3'

    serial_ = serial.Serial()

    def __init__(self):
        self.serial_.boudrate = self.boudrate
        self.serial_.port = self.com_port

        try:
            self.serial_.open()
            print("Connected to port: "+self.com_port)
        except:
            pass

