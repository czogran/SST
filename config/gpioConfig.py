import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

laserLeft = 16
laserRight = 26

output1 = 27
output2 = 22
pwm_output = 17

outputEngine1 = 10
outputEngine2 = 9
pwmOutputEngine = 11

GPIO.setup(laserLeft, GPIO.OUT)
GPIO.setup(laserRight, GPIO.OUT)

GPIO.setup(outputEngine1, GPIO.OUT)
GPIO.setup(outputEngine2, GPIO.OUT)
GPIO.setup(pwmOutputEngine, GPIO.OUT)

GPIO.setup(output1, GPIO.OUT)
GPIO.setup(output2, GPIO.OUT)
GPIO.setup(pwm_output, GPIO.OUT)

# GPIO.output(output1, GPIO.HIGH)
# GPIO.output(output2, GPIO.LOW)
#
# GPIO.output(output11, GPIO.LOW)
# GPIO.output(output22, GPIO.HIGH)

pwm_value = GPIO.PWM(pwm_output, 1000)
pwm_value.start(1)

pwm_value2 = GPIO.PWM(pwmOutputEngine, 1000)
pwm_value2.start(0)

GPIO.output(output1, GPIO.LOW)
GPIO.output(output2, GPIO.LOW)

GPIO.output(laserLeft, GPIO.LOW)
GPIO.output(laserRight, GPIO.LOW)


def turnOn(sleepTime):
    # TODO pinout
    # GPIO.output(laserLeft, GPIO.HIGH)
    GPIO.output(output1, GPIO.HIGH)
    GPIO.output(output2, GPIO.LOW)

    time.sleep(sleepTime)

    # GPIO.output(laserLeft, GPIO.LOW)
    GPIO.output(output1, GPIO.LOW)
    GPIO.output(output2, GPIO.LOW)


def transmitHigh(sleepTime):
    GPIO.output(output1, GPIO.HIGH)
    GPIO.output(output2, GPIO.LOW)
    time.sleep(sleepTime)


def transmitLow(sleepTime):
    GPIO.output(output1, GPIO.LOW)
    GPIO.output(output2, GPIO.LOW)
    time.sleep(sleepTime)


def transmitHighLeft(sleepTime):
    GPIO.output(laserLeft, GPIO.HIGH)
    time.sleep(sleepTime)


def transmitLowLeft(sleepTime):
    GPIO.output(laserLeft, GPIO.LOW)
    time.sleep(sleepTime)

def transmitHighRight(sleepTime):
    GPIO.output(laserRight, GPIO.HIGH)
    time.sleep(sleepTime)


def transmitLowRight(sleepTime):
    GPIO.output(laserRight, GPIO.LOW)
    time.sleep(sleepTime)
