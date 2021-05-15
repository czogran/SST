import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
grandparentdir = os.path.dirname(parentdir)
sys.path.insert(0, grandparentdir)

from config.gpioConfig import transmitHigh, transmitLow

import RPi.GPIO as GPIO

from hamming import hammingCodes, appendParityBits, hammingCorrection
import time

print("ASCII TRANSMITTER")

file = open('message.txt')
fileContent = file.read()
file.close()


def transmit(bite):
    sleepTime = 0.075

    if bite == 1:
        transmitHigh(sleepTime)
    elif bite == 0:
        transmitLow(sleepTime)

    elif bite == '1':
        transmitHigh(sleepTime)
    elif bite == '0':
        transmitLow(sleepTime)


for i in range(10):
    transmit('1')

for letter in fileContent:
    code = bin(int.from_bytes(letter.encode(), 'big'))

    if code == " ":

        code = '00' + code[2:]
    else:
        code = '0' + code[2:]

    print(letter)
    print(code)
    code = hammingCodes(code)
    print(code)
    print(hammingCorrection(code))


    for bite in (code):
        # print(bite)
        transmit(bite)
    print("")

GPIO.cleanup()
