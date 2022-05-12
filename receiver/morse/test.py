import RPi.GPIO as GPIO
import time
morseTransmitterDictionary = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': ' '}




morseReceiverDictionary = {'.-': 'A', '-...': 'B', '-.-.': 'C',
                   '-..': 'D', '.': 'E', '..-.': 'F',
                   '--.': 'G', '....': 'H', '..': 'I',
                   '.---': 'J', '-.-': 'K', '.-..': 'L',
                   '--': 'M', '-.': 'N', '---': 'O',
                   '.--.': 'P', '--.-': 'Q', '.-.': 'R',
                   '...': 'S', '-': 'T', '..-': 'U',
                   '...-': 'V', '.--': 'W', '-..-': 'X',
                   '-.--': 'Y', '--..': 'Z', '.----': '1',
                   '..---': '2', '...--': '3', '....-': '4',
                   '.....': '5', '-....': '6', '--...': '7',
                   '---..': '8', '----.': '9', '-----': '0',
                   '--..--': ', ', '.-.-.-': '.', '..--..': '?',
                   '-..-.': '/', '-....-': '-', '-.--.': '(',
                   '-.--.-': ')', ' ': ' '}

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
dwntime = start_time
prnt = False
while True:
    snap = GPIO.input(detectPin)
    if prev != snap and time.time() - max(uptime, dwntime) > sanity:
        prev = snap
        prnt = True #flaga do printowania wiadomosci
        if not snap:
            uptime = time.time()
            if 2.6 * dot < uptime - dwntime:
                print(char)
                try:
                    print(morseReceiverDictionary[char])
                    sentence = sentence + morseReceiverDictionary[char]
                except KeyError:
                    print(char)
                char = ""
        else:
            dwntime = time.time()
            if dwntime - uptime > 1.6 * dot:
                char = char + '-'
            else:
                char = char + '.'
    if prnt and time.time() - dwntime > 6.6 * dot:
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
