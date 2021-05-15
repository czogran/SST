import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
grandparentdir = os.path.dirname(parentdir)
sys.path.insert(0, grandparentdir)

from config.gpioConfig import transmitHigh, transmitLow

import RPi.GPIO as GPIO
import time

print("ASCII TRANSMITTER")

file = open('message.txt')
fileContent = file.read().upper()
file.close()

# print(bin(int.from_bytes(" ".encode(), 'big')))


def transmit(bite):
    sleepTime = 0.1
    print(bite)
    if bite == '1':
        transmitHigh(sleepTime)
    elif bite == '0':
        transmitLow(sleepTime)


code = bin(int.from_bytes(fileContent.encode(), 'big'))

# code= code[2:]
code= '0'+code[2:]
# print(code)
print("code")
print(code)

for i in range(10):
    transmit('1')

for bite in str(code):
    # try:
    #     print(bite)

    transmit(bite)
    # except:
    #     pass

GPIO.cleanup()
