def znajdzPalindrom(myInput):
    if type(myInput) != int:
        return "Podaj inta"
    for liczba in range(myInput, 1, -1):
        iterator = 0
        czyPalindrom = True
        for litera in str(liczba)[0:len(str(liczba))//2]:
            if czyPalindrom:
                if not (litera == str(liczba)[len(str(liczba)) - 1 - iterator]):
                    czyPalindrom = False
                iterator += 1
        if czyPalindrom:
            return liczba
    return "Palindrom nie istnieje" #Nigdy nie jest prawdą

# Niestety ten problem jest zbyt złożony obliczeniowo i rekurencja temu nie podoła

#def znajdzPalindromV2(myInput):
#    if type(myInput) != int:
#        return "Podaj inta"
#    if str(myInput)[:len(str(myInput))//2] != str(myInput)[len(str(myInput)) - 1:len(str(myInput)) - len(str(myInput))//2 - 1:-1]:
#        return znajdzPalindromV2(myInput - 1)
#    else:
#        return myInput

print(znajdzPalindrom(10003))
print(znajdzPalindrom(150))
print(znajdzPalindrom("es"))
zmienna = 2147483647
print(znajdzPalindrom(zmienna))
