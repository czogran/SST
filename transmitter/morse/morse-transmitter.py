from morseDictionary import morseTransmitterDictionary
import os, sys, inspect

# importing configuration
currentDirectory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentDirectory = os.path.dirname(currentDirectory)
grandparentDirectory = os.path.dirname(parentDirectory)
sys.path.insert(0, grandparentDirectory)

from config.gpioConfig import turnOn
import RPi.GPIO as GPIO
import time

print("MORSE TRANSMITTER")

# getting message for sending
file = open('message.txt')
message = file.read().upper()
file.close()

# Record-> factor = 0.02
# Determines how long signal takes
factor = 0.2

# Morse signal parameters
dotLength = 1 * factor
lineLength = 3 * factor
codeSpace = 1 * factor
signSpace = 3 * factor - codeSpace
wordSpace = 7 * factor

prev = time.time()

def transmit(code):
    global prev
    prev = time.time()
    if code == ' ':
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


for letter in message:
    try:
        code = morseTransmitterDictionary[letter]
        print(letter)

        transmit(code)
    except:
        pass

# cleaning pins after script execution
GPIO.cleanup()
