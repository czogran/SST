import os, sys, inspect

# importing configuration
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
grandparentdir = os.path.dirname(parentdir)
sys.path.insert(0, grandparentdir)

from config.gpioConfig import transmitHigh, transmitLow

import RPi.GPIO as GPIO

print("ASCII TRANSMITTER")

file = open('message.txt')
fileContent = file.read().upper()
file.close()

sleepTime = 0.2

def transmit(bite):
    print(bite)
    if bite == '1':
        transmitHigh(sleepTime)
    elif bite == '0':
        transmitLow(sleepTime)


code = bin(int.from_bytes(fileContent.encode(), 'big'))

# Removing incorrect sequence start
code = '0' + code[2:]

print("code")
print(code)

# Start frequency
for i in range(10):
    transmit('1')

for bite in str(code):
    transmit(bite)

GPIO.cleanup()
