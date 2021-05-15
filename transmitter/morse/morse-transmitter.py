from morseDictionary import morseTransmitterDictionary
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
grandparentdir = os.path.dirname(parentdir)
sys.path.insert(0, grandparentdir)

from config.gpioConfig import turnOn

import RPi.GPIO as GPIO
import time

print("TRANSMITTER")

file = open('message.txt')
fileContent = file.read().upper()
file.close()

factor = 0.01

dotLength = 1 * factor
lineLength = 3 * factor
codeSpace = 1 * factor
signSpace = 3 * factor - codeSpace
wordSpace = 7 * factor

prev = time.time()


def transmit(code):
    global prev
    # print(time.time()-prev)
    prev = time.time()
    if code == ' ':
        # print("space")
        time.sleep(wordSpace)
        return

    for mark in code:
        if mark == ".":
            print('.', end='')
            turnOn(dotLength)

        elif mark == "-":
            print("-", end=" ")
            turnOn(lineLength)
        time.sleep(codeSpace)

    time.sleep(signSpace)
    print("")
    # print("end")


for letter in fileContent:
    try:
        code = morseTransmitterDictionary[letter]
        print(letter)

        transmit(code)
    except:
        pass

GPIO.cleanup()
