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

# GPIO.output(output1, GPIO.HIGH)
# GPIO.output(output2, GPIO.LOW)
#
# GPIO.output(output11, GPIO.LOW)
# GPIO.output(output22, GPIO.HIGH)

pwm_value = GPIO.PWM(pwm_output, 1000)
pwm_value.start(1)

pwm_value2 = GPIO.PWM(pwm_output2, 1000)
pwm_value2.start(0)

GPIO.output(output1, GPIO.LOW)
GPIO.output(output2, GPIO.LOW)

def turnOn(sleepTime):
    # TODO pinout
    GPIO.output(output1, GPIO.HIGH)
    GPIO.output(output2, GPIO.LOW)

    time.sleep(sleepTime)

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
