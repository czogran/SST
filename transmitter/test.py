import RPi.GPIO as GPIO
import time

print("transmitter")

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

laserLeft = 16
laserRight = 26

output1 = 27
output2 = 22
pwm_output = 17

outputEngine1 = 10
outputEngine2 = 9
pwm_outputEngine = 11

GPIO.setup(laserLeft, GPIO.OUT)
# pwm_value1 = GPIO.PWM(laserLeft, 0.5)
# pwm_value1.start(50)

GPIO.setup(laserRight, GPIO.OUT)

GPIO.setup(outputEngine1, GPIO.OUT)
GPIO.setup(outputEngine2, GPIO.OUT)
GPIO.setup(pwm_outputEngine, GPIO.OUT)

GPIO.setup(output1, GPIO.OUT)
GPIO.setup(output2, GPIO.OUT)
GPIO.setup(pwm_output, GPIO.OUT)

GPIO.output(output1, GPIO.HIGH)
GPIO.output(output2, GPIO.LOW)

GPIO.output(outputEngine1, GPIO.LOW)
GPIO.output(outputEngine2, GPIO.HIGH)

# pwm_value1 = GPIO.PWM(laser1, 1)
# pwm_value1.start(50)
#
# pwm_value = GPIO.PWM(laser2, 1)
# pwm_value.start(50)

pwm_value = GPIO.PWM(pwm_output, 300)
pwm_value.start(75)

pwm_value2 = GPIO.PWM(pwm_outputEngine, 1000)
pwm_value2.start(0)

sleep_time = 1

print("start")

# for i in range(10):
while True:
    print("on")

    GPIO.output(laserLeft, GPIO.HIGH)
    GPIO.output(laserRight, GPIO.HIGH)
    time.sleep(sleep_time / 2)
    GPIO.output(output1, GPIO.HIGH)
    GPIO.output(output2, GPIO.LOW)
    time.sleep(sleep_time)
    print("off")
    GPIO.output(laserLeft, GPIO.LOW)
    GPIO.output(laserRight, GPIO.LOW)
    time.sleep(sleep_time / 2)

    GPIO.output(output1, GPIO.LOW)
    GPIO.output(output2, GPIO.LOW)
    time.sleep(sleep_time)

# pwm_value = GPIO.PWM(pwm_output, 1000)
# pwm_value.start(pwm_value)
