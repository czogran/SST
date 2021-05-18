import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

detectPinLeft = 17
detectPinMiddle = 14
detectPinRight = 5
GPIO.setup(detectPinLeft, GPIO.IN)
GPIO.setup(detectPinMiddle, GPIO.IN)
GPIO.setup(detectPinRight, GPIO.IN)

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
   global buffer

   buffer.append(str(1-GPIO.input(detectPinLeft)))
   buffer.append(str(1-GPIO.input(detectPinRight)))

   if len(buffer)==8:
      bufferContent = "".join(buffer)
      print(buffer)
      print(bufferContent)
      try:
         n = int(bufferContent, 2)
         print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
      except:
         print("decode Error")
      buffer = []


GPIO.add_event_detect(detectPinMiddle, GPIO.BOTH, callback=my_callback, bouncetime=debounceTime)

time.sleep(30)