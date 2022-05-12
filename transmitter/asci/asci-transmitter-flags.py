import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
grandparentdir = os.path.dirname(parentdir)
sys.path.insert(0, grandparentdir)

from config.gpioConfig import transmitHigh, transmitLow

import RPi.GPIO as GPIO
import time

print("ASCII TRANSMITTER WITH FLAG ON THE START")

file = open('message.txt')
fileContent = file.read().upper()
file.close()


def transmit(bite):
    sleepTime = 0.5
    if bite == '1':
        transmitHigh(sleepTime)
    elif bite == '0':
        transmitLow(sleepTime)


code = bin(int.from_bytes(fileContent.encode(), 'big'))

# Removing incorrect sequence start
code = '0' + code[2:]

for index,bite in enumerate(str(code)):
    if index % 8 == 0:
        print(bite)
        transmit(1)

    transmit(bite)

GPIO.cleanup()
