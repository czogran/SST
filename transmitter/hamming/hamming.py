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
        total = 0
        for j in range(int(k), len(list1) + 1, 2 * int(k)):
            for p in range(0, int(k)):
                if j - 1 + p >= len(list1):
                    break

                total = total + int(list1[j - 1 + p])
                # if k == 8:
                #     print("a", j + p, total)
        if total % 2 > 0:
            list1[int(
                k) - 1] = 1  # to check even parity summing up all the elements in sublist and if summ is even than even parity else odd parity
        i += 1
    # print(data)
    # print(list1)
    return list1
