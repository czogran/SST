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
    # if not snap:
    #     if not prev:
    #         ones = ones + 1
    #     else:
    #         zeros =
    # time.sleep(0)
    # if not receiving:
    #     if not snap:
    #         start = time.time()
    #         receiving = True
    #         halting = False
    # elif snap:
    #     receiving = False
    #     if time.time() - start < 3:
    #         mess.append(0)
    #     else:
    #         mess.append(1)
    #     print(mess)
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
    # if time.time() - prev_time > 10:
    #     print(i)
    #     prev_time = time.time()
    #     chars = []
    #     for b in range(int(len(mess) / 8)):
    #         byte = mess[b * 8:(b + 1) * 8]
    #         chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    #     print(''.join(chars))
    #     print(mess)
print("ok")

GPIO.cleanup()
