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
    snap = GPIO.input(detect)
    if prev != snap:
        prnt = True #flaga do printowania wiadomosci
        if not snap:
            i = i + 1
            uptime = time.time()
            if 2.5 * dot < uptime - dwntime < 6.5 * dot:    #to nic nie robi
                rdy = True
        else:
            dwntime = time.time()
            if dwntime - uptime > 2 * dot:
                mess = mess + '-'
            else:
                mess = mess + '.'

    prev = snap
    if prnt and time.time() - dwntime > 6.5 * dot:
        print(mess)
        mess = ""
        prnt = False
print("ok")

GPIO.cleanup()
