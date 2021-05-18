import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
detectPin = 14
GPIO.setup(detectPin, GPIO.IN)

samplesPerByte = 5
samplingPeriod = 0.2 / samplesPerByte
buffer = []
message = ""
start = time.time()
begin = False

bitLength = 1000
debounceTime = 2

bitCounter = 0


# Define a threaded callback function to run in another thread when events are detected
def my_callback(channel):
    global prevTime
    global char
    global sentence
    global word
    global bitCounter
    currentTime = time.time()

    timeDiff = currentTime - prevTime

    print(timeDiff)
    ++bitCounter
    # Rising edge, laser from on to off (it is reversed!)
    if GPIO.input(channel):  # if port 25 == 1
        bits = int(round(sum(timeDiff) / bitLength))

        for bit in range(bits):
            buffer.append(1)
    # Falling edge, laser from off to on
    else:  # if port 14 != 1
        bits = int(round(sum(timeDiff) / bitLength))
        for bit in range(bits):
            buffer.append(0)
    prevTime = currentTime

# channel = GPIO.wait_for_edge(detectPin, GPIO.FALLING, timeout=5000)


GPIO.add_event_detect(detectPin, GPIO.BOTH, callback=my_callback, bouncetime=debounceTime)