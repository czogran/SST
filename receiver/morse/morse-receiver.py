import RPi.GPIO as GPIO
import time
from morseReceiverDictionary import morseReceiverDictionary


GPIO.setmode(GPIO.BCM)
detectPin = 14
dot = 0.05
sanity = 0.005
prev = True
char = ""
sentence = ""
GPIO.setup(detectPin, GPIO.IN)
start_time = time.time()
uptime = start_time
downtime = start_time
prnt = False

while True:
    snap = GPIO.input(detectPin)
    if prev != snap and time.time() - max(uptime, downtime) > sanity:
        prev = snap
        prnt = True #flaga do printowania wiadomosci
        if not snap:
            uptime = time.time()
            if 2.6 * dot < uptime - downtime:
                print(char)
                try:
                    print(morseReceiverDictionary[char])
                    sentence = sentence + morseReceiverDictionary[char]
                except KeyError:
                    print(char)
                char = ""
        else:
            downtime = time.time()
            if downtime - uptime > 1.6 * dot:
                char = char + '-'
            else:
                char = char + '.'
    if prnt and time.time() - downtime > 6.6 * dot:
        print(char)
        try:
            print(morseReceiverDictionary[char])
            sentence = sentence + morseReceiverDictionary[char]
        except KeyError:
            print(char)
        char = ""
        print(sentence)
        sentence = ""
        prnt = False
print("ok")

GPIO.cleanup()
