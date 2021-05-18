import RPi.GPIO as GPIO
import time

def noOfParityBits(noOfBits):
    i = 0
    while 2. ** i <= noOfBits + i:  # (power of 2 + parity bits laready  counted) that is for 4 bit of dataword requires 3 bit of parity bits
        i += 1
    return i


# function to genrate no of parity bits in while correction of hamming codes returns no of parity bits in given size of code word
def noOfParityBitsInCode(noOfBits):
    i = 0
    while 2. ** i <= noOfBits:
        i += 1

    return i


# parameter:data
# returns a list with parity bits position is 0 that is position which are power of 2 are 0

def appendParityBits(data):
    n = noOfParityBits(len(data))  # no of parity bits required for given length of data
    i = 0  # loop counter
    j = 0  # no of parity bits
    k = 0  # no of data bits
    list1 = list()
    while i < n + len(data):
        if i == (2. ** j - 1):
            list1.insert(i, 0)
            j += 1
        else:
            list1.insert(i, data[k])
            k += 1
        i += 1
    return list1

def hammingCodes(data):
    n = noOfParityBits(len(data))
    list1 = appendParityBits(data)  # list with parity bits at appropriate position
    i = 0  # loop counter
    k = 1  # 2 to the power kth parity bit
    while i < n:
        k = 2. ** i
        j = 1
        total = 0
        while j * k - 1 < len(list1):
            if j * k - 1 == len(list1) - 1:  # if lower index is last one to be considered in sub list then
                lower_index = j * k - 1
                temp = list1[int(lower_index):len(list1)]
            elif (j + 1) * k - 1 >= len(list1):
                lower_index = j * k - 1
                temp = list1[int(lower_index):len(list1)]  # if list's size is smaller than boundary point
            elif (j + 1) * k - 1 < len(list1) - 1:
                lower_index = (j * k) - 1
                upper_index = (j + 1) * k - 1
                temp = list1[int(lower_index):int(upper_index)]

            total = total + sum(int(e) for e in temp)  # do the sum of sub list for corresponding parity bits
            j += 2  # increment by 2 beacause we want alternative pairs of numberss from list
        if total % 2 > 0:
            list1[int(
                k) - 1] = 1  # to check even parity summing up all the elements in sublist and if summ is even than even parity else odd parity
        i += 1
    return list1


def hammingCorrection(data):
    n = noOfParityBitsInCode(len(data))
    i = 0
    list1 = list(data)
    errorthBit = 0
    while i < n:
        k = 2. ** i
        print("k: "+str(k))
        total = 0
        for j in range(int(k), len(list1) + 1, 2*int(k)):
            print("j:" + str(j))
            for p in range(0, int(k)):
                if j - 1 + p >= len(list1):
                    break
                total = total + int(list1[j - 1 + p])
                print(j - 1 + p)
        if total % 2 > 0:
            errorthBit = errorthBit + k  # to check even parity summing up all the elements in sublist and if summ is even than even parity else odd parity
        i += 1
    if errorthBit >= 1:
        # toggle the corrupted bit
        if list1[int(errorthBit - 1)] == '0' or list1[int(errorthBit - 1)] == 0:
            list1[int(errorthBit - 1)] = 1
        else:
            list1[int(errorthBit - 1)] = 0
    list2 = list()
    i = 0
    j = 0
    k = 0
    # returning only data from codeword that is ignoring parity bits
    while i < len(list1):  # returning only data bits
        if i != ((2 ** k) - 1):
            temp = list1[int(i)]
            list2.append(str(temp))
            j += 1
        else:
            k += 1
        i += 1
    return list2
#01010011
print("RECEIVER")
print(hammingCodes('01010011'))
#mess = '000110100011'
mess = '100110100011'
mess = hammingCorrection(mess)
print(mess)
GPIO.setmode(GPIO.BCM)
detectPins = [17, 5]#14 default
synchPin = 14
prev = True
sanity = 0.001
mess = ''
messb = ''
for p in detectPins:
    GPIO.setup(p, GPIO.IN)
reads = [0, 0]
GPIO.setup(synchPin, GPIO.IN)
start_time = time.time()
prevTime = start_time
prnt = False
while True:
    snapSynch = GPIO.input(synchPin)
    if prev != snapSynch:
        for p in range(0, len(detectPins)):
            reads[p] = GPIO.input(detectPins[p])
        temp = time.time()
        if temp - prevTime < sanity:
            continue
        prevTime = temp
        prev = snapSynch
        for r in reads:
            if r:
                mess = mess + '0'
            else:
                mess = mess + '1'
        if len(mess) == 12:
            #print(mess)
            print("raw: " + mess)
            mess = hammingCorrection(mess)
            word = ""
            for m in mess:
                word = word + str(m)
            try:
                n = int(word, 2)
                print("sign: ", n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('ascii'), " byte: ", mess)
            except:
                print("Unable to decode")
                mess = ''
            mess = ''
print("ok")

GPIO.cleanup()
