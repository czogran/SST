import RPi.GPIO as GPIO
import time

# setup gpio pins
GPIO.setmode(GPIO.BCM)
detectPin = 14
GPIO.setup(detectPin, GPIO.IN)

buffer = []
message = ""
start = time.time()

#duration of one bite
bitLength = 1000
debounceTime = 2

# Define a threaded callback function to run in another thread when events are detected
def my_callback(channel):
    global prevTime
    global char
    global sentence
    global word
    currentTime = time.time()

    timeDiff = currentTime - prevTime

    # Rising edge, laser from on to off (it is reversed!)
    if GPIO.input(channel):
        bits = int(round(sum(timeDiff) / bitLength))

        for bit in range(bits):
            buffer.append(1)
    # Falling edge, laser from off to on
    else:
        bits = int(round(sum(timeDiff) / bitLength))
        for bit in range(bits):
            buffer.append(0)
    prevTime = currentTime

GPIO.add_event_detect(detectPin, GPIO.BOTH, callback=my_callback, bouncetime=debounceTime)