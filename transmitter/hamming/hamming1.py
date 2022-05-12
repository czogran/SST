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
    list1 = list(data)
    dataLength = len(list1)

    j = 1
    for i in range(n):
        index = dataLength - 2 ** (i) + j
        j += 1
        list1.insert(index, 9)
    print("list1", list1)
    return list1

def appendParityBits(data):
    n = noOfParityBits(len(data))  # no of parity bits required for given length of data
    list1 = list(data)
    dataLength = len(list1)

    j = 1
    for i in range(n):
        index = dataLength - 2 ** (i) + j
        j += 1
        list1.insert(index, 9)
    print("list1", list1)
    return list1

def appendParityBits1(data):
    n = noOfParityBits(len(data))  # no of parity bits required for given length of data
    list1 = list(data)
    for i in range(n):
        index = 2 ** i - 1
        list1.insert(index, 9)
    print("list1", list1)
    return list1

appendParityBits1("01010011")


def hammingCorrection1(letter):
    value = int.from_bytes(letter.encode(), 'big')
    biteCode = bin(value)

    biteCode = '0' + biteCode[2:]

    # print("biteCode",biteCode)

    biteCode = appendParityBits(biteCode)
    print("biteCodeAppended", biteCode)

    parityBitsAmount = noOfParityBitsInCode(len(biteCode))
    parityBitsValues = [0] * (parityBitsAmount)

    print("a", (parityBitsValues))
    print("a", (parityBitsAmount))
    codeLength = len(biteCode)

    for i in range(parityBitsAmount, 0, -1):
        print("i", i)
        for j in range(codeLength):
            k = 2 ** (i - 1)
            if j & k == k:
                if (k == 4):
                    print(i, k, j, codeLength - j, biteCode[codeLength - j])
                parityBitsValues[i - 1] = parityBitsValues[i - 1] + int(biteCode[codeLength - j])

    biteCode = list(biteCode)

    codeLength = len(biteCode)
    for i in range(parityBitsAmount):
        print(i)
        biteCode[codeLength - 2 ** i] = parityBitsValues[i]
        # print(parityBitsAmount-i-1)
        # biteCode[2 ** i - 1]=parityBitsValues[parityBitsAmount-i-1]
    print(value)
    print(biteCode)
    print("w", parityBitsValues)
    print(parityBitsValues[3])


# hammingCorrection1("S")


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
            print
            total, j
            j += 2  # increment by 2 beacause we want alternative pairs of numberss from list
        if total % 2 > 0:
            list1[int(
                k) - 1] = 1  # to check even parity summing up all the elements in sublist and if summ is even than even parity else odd parity
            print
            "Element is ", list1[int(k) - 1], k
        i += 1
    return list1


# Prodecure is same as above function the minor change is we need to identify if error exists then on which bit
# To do so we will identify that which parity bits are odd parities(incorrect) we will add all parities bit position(weight) to get position of corrupted bit
# E.g.: if p1 and p4 are odd parity but p2 is even(correct) so errorthbit=1+4=5 that is 5th bit(4th index of list) is wrong toggle it and display the data
def hammingCorrection(data):
    n = noOfParityBitsInCode(len(data))
    i = 0
    list1 = list(data)
    # print("list1",list1)
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
            # print ("tt",total, j)
            j += 2  # increment by 2 beacause we want alternative pairs of numberss from list
        if total % 2 > 0:
            errorthBit += k  # to check even parity summing up all the elements in sublist and if summ is even than even parity else odd parity
        i += 1
    if errorthBit >= 1:
        print("error in ", errorthBit, " bit after correction data is ")
        # toggle the corrupted bit
        if list1[int(errorthBit - 1)] == '0' or list1[int(errorthBit - 1)] == 0:
            list1[int(errorthBit - 1)] = 1
        else:
            list1[int(errorthBit - 1)] = 0
    else:
        print("No error")
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
