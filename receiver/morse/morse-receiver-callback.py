import RPi.GPIO as GPIO
import time
from morseReceiverDictionary import morseReceiverDictionary

detectPin = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(detectPin, GPIO.IN)

# Record-> factor = 0.02
factor = 0.05
dotLength = 1 * factor
# Record-> debounceTime = 2
debounceTime = 1

print("start")


prevTime = 0

char = ""
sentence = ""
word = ""


# Define a threaded callback function to run in another thread when events are detected
def my_callback(channel):
    global prevTime
    global char
    global sentence
    global word
    currentTime = time.time()

    timeDiff = currentTime - prevTime

    # Rising edge, laser from on to off (it is reversed!)
    if GPIO.input(channel):  # if port 25 == 1
        if timeDiff > 1.6 * dotLength:
            char = char + '-'
        else:
            char = char + '.'
    # Falling edge, laser from off to on
    else:  # if port 14 != 1
        if timeDiff > 6.6 * dotLength:
            try:
                print(morseReceiverDictionary[char])
                word = word + morseReceiverDictionary[char]
            except KeyError:
                print("error", char)
            sentence = sentence + word + " "
            print("word", word)
            print("sentence", sentence)
            word = ""
            char = ""
        elif timeDiff > 1.6 * dotLength:
            try:
                print(morseReceiverDictionary[char])
                word = word + morseReceiverDictionary[char]
            except KeyError:
                print("error", char)
            char = ""
    prevTime = currentTime


# else is happening in the program, the function my_callback will be run
GPIO.add_event_detect(detectPin, GPIO.BOTH, callback=my_callback, bouncetime=debounceTime)

try:
    time.sleep(40)  # wait 40 seconds
finally:  # this block will run no matter how the try block exits
    GPIO.cleanup()  # clean up after yourself
