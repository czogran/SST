import time
# from morse.morseDictionary import morseDictionary
# import gpioConfig
# from gpioConfig import turnOn



import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

output1 = 27
output2 = 22
pwm_output = 17

output11 = 10
output22 = 9
pwm_output2 = 11

GPIO.setup(output11, GPIO.OUT)
GPIO.setup(output22, GPIO.OUT)
GPIO.setup(pwm_output2, GPIO.OUT)

GPIO.setup(output1, GPIO.OUT)
GPIO.setup(output2, GPIO.OUT)
GPIO.setup(pwm_output, GPIO.OUT)

GPIO.output(output1, GPIO.HIGH)
GPIO.output(output2, GPIO.LOW)

GPIO.output(output11, GPIO.LOW)
GPIO.output(output22, GPIO.HIGH)

pwm_value = GPIO.PWM(pwm_output, 1000)
pwm_value.start(1)

pwm_value2 = GPIO.PWM(pwm_output2, 1000)
pwm_value2.start(0)

def turnOn(sleepTime):
    # TODO pinout
    GPIO.output(output1, GPIO.HIGH)
    GPIO.output(output2, GPIO.LOW)

    time.sleep(sleepTime)

    GPIO.output(output1, GPIO.LOW)
    GPIO.output(output2, GPIO.LOW)





morseDictionary = {'A': '.-', 'B': '-...',
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









file = open('./message.txt')
fileContent = file.read().upper()
file.close()

dotLength = 1
lineLength = 3
codeSpace = 1
signSpace = 3
wordSpace = 7

def transmit(code):
    for mark in code:
        if mark == ".":
            print("dot")
            turnOn(dotLength)
        elif mark == "-":
            turnOn(lineLength)
            time.sleep(codeSpace)
    if code == ' ':
        time.sleep(wordSpace)
        print("space")
    time.sleep(signSpace)


for letter in fileContent:
    code = morseDictionary[letter]
    print(code)
    transmit(code)
    transmit(code)