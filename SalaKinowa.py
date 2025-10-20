class Kino:
    def __init__(self):
        self.siedzenia = [["*" for i in range(self.siedzeniaWidth)]for j in range(self.siedzeniaHeight)]

    def rezerwoj(self, numerMiejsca):
        if(self.siedzenia[ord(numerMiejsca[0])-97][int(numerMiejsca[1:]) - 1] == "*"):
            self.siedzenia[ord(numerMiejsca[0])-97][int(numerMiejsca[1:]) - 1] = "x"
            print("Miejsce zarezerwowane pomyslnie.")
        else:
            print("Blad. Nie można zarezerwować miejsca.")

    def anulujRezerwacje(self, numerMiejsca):
        if (self.siedzenia[ord(numerMiejsca[0]) - 97][int(numerMiejsca[1:]) - 1] == "x"):
            self.siedzenia[ord(numerMiejsca[0]) - 97][int(numerMiejsca[1:]) - 1] = "*"
            print("Rezerwacja anulowana pomyslnie.")
        else:
            print("Blad. Nie można anulowac rezerwacji miejsca.")

    def wyswietl(self):
        for i in range(self.siedzeniaWidth):
            print(chr(97 + i) + " ", end="")
            for j in range(self.siedzeniaHeight):
                print(self.siedzenia[i][j], end="")
            print("\n", end="")

    siedzenia = list()
    siedzeniaWidth = 10
    siedzeniaHeight = 10

czyKoniec = False
kino = Kino()
while(not czyKoniec):
    print("Podaj komende (rezerwoj, anulujRezerwacje, wyswietl, wyjdz):")
    komenda = input()
    match komenda:
        case "rezerwoj":
            print("Podaj rzad i miejsce do zarezerwowania:")
            miejsce = input()
            kino.rezerwoj(miejsce)
        case "anulujRezerwacje":
            print("Podaj rzad i miejsce do anulowania rezerwacji:")
            miejsce = input()
            kino.anulujRezerwacje(miejsce)
        case "wyswietl":
            kino.wyswietl()
        case "wyjdz":
            print("Dziekujemy za skorzystanie z naszych uslog")
            czyKoniec = True
        case _:
            print("Nienzana komenda. Prosze podac poprawna.")
