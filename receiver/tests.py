import RPi.GPIO as GPIO
import time
import binascii
GPIO.setmode(GPIO.BCM)
detect = 14
dot = 10
receiving = False
halting = False
start = 0
start_halt = 0
dash = 0
dot = 1
i = 0
prev = True
mess = ""
GPIO.setup(detect, GPIO.IN)
start_time = time.time()
uptime = start_time
dwntime = start_time
prnt = False
prev_time = 0
while True:
    # time.sleep(1)
    snap = GPIO.input(detect)
    prnt(snap, end='')
    time.sleep(0.1)

print("ok")

GPIO.cleanup()
