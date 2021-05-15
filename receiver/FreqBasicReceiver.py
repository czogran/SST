import RPi.GPIO as GPIO
import time
import sys


# function to check no of parity bits in genration of hamming code
# return no of parity bits required to append in given size of data word
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
        j = 1
        total = 0
        while j * k - 1 < len(list1):
            if j * k - 1 == len(list1) - 1:
                lower_index = j * k - 1
                temp = list1[int(lower_index):len(list1)]
            elif (j + 1) * k - 1 >= len(list1):
                lower_index = j * k - 1
                temp = list1[int(lower_index):len(list1)]  # if list's size is smaller than boundary point
            elif (j + 1) * k - 1 < len(list1) - 1:
                lower_index = (j * k) - 1
                upper_index = (j + 1) * k - 1
                temp = list1[int(lower_index):int(upper_index)]

            total = total + sum(int(e) for e in temp)
            j += 2  # increment by 2 beacause we want alternative pairs of numberss from list
        if total % 2 > 0:
            errorthBit += k  # to check even parity summing up all the elements in sublist and if summ is even than even parity else odd parity
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
            list2.append(temp)
            j += 1
        else:
            k += 1
        i += 1
    return list2




GPIO.setmode(GPIO.BCM)
detectPin = 14
GPIO.setup(detectPin, GPIO.IN)
num = 3
schleep = 0.075/num
buffer = []
mess = ""
arr = []
start = time.time()
begin = False
while time.time() - start < 10:
    # time.sleep(1)
    snap = GPIO.input(detectPin)
    if snap:
        buffer.append(0)
    else:
        buffer.append(1)
    if len(buffer) == num:
        bit = int(round(sum(buffer)/num))
        #print(bit)
        if begin:
            mess = mess + str(bit)
            arr.append(bit)
            if len(mess) == 12:
                #print(mess)
                #mess = '0b' + mess
                try:
                    #print(hammingCorrection(mess))
                    mess = hammingCorrection(mess)
                    #print(mess)
                    word = ""
                    for m in mess:
                        word = word + m
                    n = int(word, 2)
                    print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
                except:
                    print('Oooops', sys.exc_info())
                mess = ""
                arr = []
        elif bit == 1:
            mess = mess + '1'
        buffer = []
    if mess == '1111111111' and not begin:
        begin = True
        mess = ""
        print('start')
    else:
        start = time.time()
    time.sleep(schleep)
print("ok")

GPIO.cleanup()
