import RPi.GPIO as GPIO
import time
import sys

print("ASCII RECEIVER")

GPIO.setmode(GPIO.BCM)
detectPin = 14
GPIO.setup(detectPin, GPIO.IN)

# bite length
samplesPerByte = 5
samplingPeriod = 0.2 / samplesPerByte

buffer = []
message = ""
start = time.time()
begin = False

while time.time() - start < 10:
    snap = GPIO.input(detectPin)
    if snap:
        buffer.append(0)
    else:
        buffer.append(1)
    if len(buffer) == samplesPerByte:
        bit = int(round(sum(buffer) / samplesPerByte))
        if begin:
            message = message + str(bit)
            # when one byte comes
            if len(message) == 8:
                try:
                    print(message)
                    n = int(message, 2)
                    # decoding
                    print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
                except:
                    # error in decoding
                    print('Oooops', sys.exc_info())
                message = ""
        elif bit == 1:
            message = message + '1'
        buffer = []
    # Detect start sequence
    if message == '1111111111' and not begin:
        begin = True
        message = ""
        print('start')
    else:
        start = time.time()
    time.sleep(samplingPeriod)
print("ok")

GPIO.cleanup()
