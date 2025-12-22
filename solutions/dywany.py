# zamaiana wejscia na macierz
# zprawdzanie czy dany kwadrat pomijajac ramkę jest otoczony przez pomarańczowe
# podajemy wynik


def budowanie_macierzy(wejscie):
    szerokosc, szablon = wejscie.split("\n")
    wysokosc = len(szablon) // int(szerokosc)
    macierz = []
    for i in range(int(wysokosc)):
        macierz.append(list(szablon[i * int(szerokosc) : ((i + 1) * int(szerokosc))]))
    return macierz


def czy_otoczony(macierz, wiersz_kwadrat, kolumna_kwadrat):
    for i in range(wiersz_kwadrat - 1, wiersz_kwadrat + 2):
        if macierz[i][kolumna_kwadrat] != "P":
            return False
    for i in range(kolumna_kwadrat - 1, kolumna_kwadrat + 2):
        if macierz[wiersz_kwadrat][i] != "P":
            return False
    return True


def dywan(wejscie):
    ilosc_otoczonych = 0
    macierz = budowanie_macierzy(wejscie)
    for i in range(1, len(macierz) - 1):
        for j in range(1, len(macierz[0]) - 1):
            if macierz[i][j] == "P":
                if czy_otoczony(macierz, i, j):
                    ilosc_otoczonych += 1
    return ilosc_otoczonych


assert budowanie_macierzy("3\nZZPZZZZZZ") == [
    ["Z", "Z", "P"],
    ["Z", "Z", "Z"],
    ["Z", "Z", "Z"],
]


assert dywan("10\nZZZZPPPZZZZZZPPPPPZZZZPPPPPPPZZZZPPPPPZZZZZZPPPZZZ") == 11
