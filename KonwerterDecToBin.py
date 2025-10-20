def convertDecToBin(decNumber):
    if type(decNumber) != int:
        return "Podaj inta"
    binNumber = ""
    while decNumber != 0:
        if decNumber % 2 == 0:
            binNumber += "0"
            decNumber /= 2
        else:
            binNumber += "1"
            decNumber //= 2
    return binNumber[len(binNumber)-1::-1]

print(convertDecToBin(2137))
print("100001011001\n")
print(convertDecToBin(200000))
print("110000110101000000\n")