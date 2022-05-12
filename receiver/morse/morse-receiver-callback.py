import RPi.GPIO as GPIO
import time
from morseReceiverDictionary import morseReceiverDictionary

print("MORSE RECEIVER WITH CALLBACK")

# pin setup
detectPin = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(detectPin, GPIO.IN)

# Record-> factor = 0.02
factor = 0.2

# Record-> debounceTime = 2
debounceTime = 5

# morse params, with reserve
minWordSpace = 6.6 * factor
minSignSpace = 1.6 * factor
minLineLength = 1.6 * factor

# previous time for calculating signs
prevTime = 0

char = ""
sentence = ""
word = ""

# Define a threaded callback function to run in another thread when events are detected
def eventDetectedCallback(channel):
    global prevTime
    global char
    global sentence
    global word

    currentTime = time.time()
    timeDiff = currentTime - prevTime
    prevTime = currentTime

    # Rising edge, laser from on to off (it is reversed!)
    if GPIO.input(channel):
        if timeDiff > minLineLength:
            char = char + '-'
        else:
            char = char + '.'
    # Falling edge, laser from off to on
    else:
        if timeDiff > minWordSpace:
            try:
                print(morseReceiverDictionary[char])
                word = word + morseReceiverDictionary[char]
            except KeyError:
                pass
            sentence = sentence + word + " "
            print("word", word)
            print("sentence", sentence)
            word = ""
            char = ""
        elif timeDiff > minSignSpace:
            try:
                print(morseReceiverDictionary[char])
                word = word + morseReceiverDictionary[char]
            except KeyError:
                print("error", char)
            char = ""


# add event detection
GPIO.add_event_detect(detectPin, GPIO.BOTH, callback=eventDetectedCallback, bouncetime=debounceTime)

try:
    time.sleep(40)
    print(morseReceiverDictionary[char])
    word = word + morseReceiverDictionary[char]
    sentence = sentence + word + " "
    print("word", word)
    print("sentence", sentence)
finally:
    # clean up pins
    GPIO.cleanup()
