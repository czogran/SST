import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
grandparentdir = os.path.dirname(parentdir)
sys.path.insert(0, grandparentdir)

from config.gpioConfig import transmitHigh, transmitLow, transmitHighLeft, transmitLowLeft, transmitHighRight, \
    transmitLowRight

import RPi.GPIO as GPIO
import time

print("ASCII TRANSMITTER")

file = open('message.txt')
fileContent = file.read().upper()
file.close()



code = bin(int.from_bytes(fileContent.encode(), 'big'))

# Removing incorrect sequence start
code = '0' + code[2:]

halfPeriodTime = 1


clockStateDown = True
samplesAmount = int(len(code) / 2)
byte = ""
counter = 0
transmitLow(0)

for i in range(samplesAmount):
    bite1 = code[2 * i]
    bite2 = code[2 * i + 1]


    byte = byte + bite1 + bite2;
    counter += 1
    if counter == 4:
        n = int(byte, 2)
        print("sign: ", n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(), "  byte: ", byte)
        counter = 0
        byte = ""

    if bite1 == '1':
        transmitHighLeft(0)
    elif bite1 == '0':
        transmitLowLeft(0)

    if bite2 == '1':
        transmitHighRight(0)
    elif bite2 == '0':
        transmitLowRight(0)
    time.sleep(halfPeriodTime)

    if clockStateDown:
        transmitHigh(0)
    else:
        transmitLow(0)
    time.sleep(halfPeriodTime)
    clockStateDown = not clockStateDown

GPIO.cleanup()
