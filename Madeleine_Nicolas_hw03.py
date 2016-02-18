'''
Madeleine Nicolas
mpn272
hw03
'''
#hw03q2
#converts decimal numbers into binary

def convertBinary(n):
    nBinary = bin(n)
    formattedBinary = nBinary[2:]
    print(formattedBinary)

convertBinary(57)
convertBinary(123)
convertBinary(85)
convertBinary(38)

#hw03q3
#converts hex numbers in a list and prints out ASCII characters

def convertHex(hexList):
    str = ""
    for hexNum in hexList:
        numBinaryStr = bin(hexNum)
        formattedBinaryStr = numBinaryStr[2:]
        numBinaryInt = int(formattedBinaryStr, 2)
        asciiChar = chr(numBinaryInt)
        str += asciiChar
    print(str)

convertHex([0x41, 0x53, 0x43, 0x49, 0x49, 0x20, 0x77, 0x68, 0x61, 0x74, 0x20, 0x79, 0x6f, 0x75, 0x20, 0x64, 0x69, 0x64, 0x20, 0x74, 0x68, 0x65, 0x72, 0x65])
convertHex([0x39, 0x41, 0x4d, 0x20, 0x69, 0x73, 0x20, 0x74, 0x6f, 0x6f, 0x20, 0x65, 0x61, 0x72, 0x6c, 0x79, 0x20, 0x66, 0x6f, 0x72, 0x20, 0x63, 0x6c, 0x61, 0x73, 0x73])
convertHex([0x43, 0x6f, 0x6d, 0x70, 0x75, 0x74, 0x65, 0x72, 0x73, 0x20, 0x61, 0x72, 0x65, 0x20, 0x6d, 0x61, 0x67, 0x69, 0x63])
convertHex([0x57, 0x68, 0x61, 0x74, 0x20, 0x74, 0x68, 0x65, 0x20, 0x68, 0x65, 0x78, 0x3f])

#hw03q4
#converts binary numbers to decimal then to hex representation

def convertBinToHex(binString):
    decimal = int(binString, 2)
    hexadecimal = hex(decimal)
    print(hexadecimal)

convertBinToHex('00001011101011101101111010101101')
convertBinToHex('11001010111111101111101011001110')
convertBinToHex('10111110111011111101000000001101')
convertBinToHex('11111111111111111001000001100010')

#hw03q5
#convert base 8 integer into decimal

def convertOctToDec(octInt):
    octStr = str(octInt)
    lenOctStr = len(octStr)
    decInt = 0
    power = lenOctStr - 1
    base = 8
    for digit in octStr:
        digitVal = int(digit) * (base**power)
        decInt += digitVal
        power -= 1
    print(decInt)

convertOctToDec(10)
convertOctToDec(42)
convertOctToDec(77)
convertOctToDec(113)

