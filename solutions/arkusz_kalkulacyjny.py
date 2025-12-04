from string import ascii_uppercase


def arkusz(wejscie):
    macierz = zapelnianie_macierzy(wejscie)
    pelne = liczenie_pelnych_komorek(macierz)
    return pelne


def zapelnianie_macierzy(wejscie):
    odszyfrowane, najwiekszy_wiersz, najwieksza_kolumna = odszyfrowanie_pozycji(wejscie)
    macierz = robienie_macierzy(najwiekszy_wiersz, najwieksza_kolumna)
    zakres = []
    for i in range(0, len(odszyfrowane), 2):
        zakres.append(odszyfrowane[i])
        zakres.append(odszyfrowane[i + 1])
        macierz = zapelnianie_czworokata(zakres, macierz)
        zakres = []
    return macierz


def zapelnianie_czworokata(zakres, macierz):
    for j in range(zakres[0][0], zakres[1][0] + 1):
        for k in range(zakres[0][1], zakres[1][1] + 1):
            macierz[k][j] = True
    return macierz


def robienie_macierzy(najwiekszy_wiersz, najwieka_kolumna):
    return [
        [False for _ in range(najwieka_kolumna + 1)]
        for _ in range(najwiekszy_wiersz + 1)
    ]


# assert zapelnianie_czworokata([[0, 0], [1, 2]], robienie_macierzy(2, 3)) == [
#     [True, True, True, False],
#     [True, True, True, False],
#     [False, False, False, False],
# ]


def odszyfrowanie_pozycji(wejscie: str):
    pary = wejscie.split(" ")
    najwieksza_kolumna = 0
    najwiekszy_wiersz = 0
    odszyfrowane = []
    for i in range(len(pary)):
        poczatek_zakresu, koniec_zakresu = para_na_komorki(pary[i])  # A1, C2
        wspolrzedne_poczatket = komorka_na_wspolrzendne2(poczatek_zakresu)
        wspolrzedne_koniec = komorka_na_wspolrzendne2(koniec_zakresu)
        odszyfrowane.append(wspolrzedne_poczatket)  # 00
        odszyfrowane.append(wspolrzedne_koniec)  # 21
        if wspolrzedne_koniec[1] > najwiekszy_wiersz:
            najwiekszy_wiersz = wspolrzedne_koniec[1]
        if wspolrzedne_koniec[0] > najwieksza_kolumna:
            najwieksza_kolumna = wspolrzedne_koniec[0]
    return odszyfrowane, najwiekszy_wiersz, najwieksza_kolumna


def liczenie_pelnych_komorek(macierz):
    puste = 0
    for i in range(len(macierz)):
        for j in range(len(macierz[0])):
            if macierz[i][j] == True:
                puste += 1
    return puste


def komorka_na_wspolrzedne(adres: str) -> tuple[int, int]:
    komorka = list(adres)
    wspolrzendne = []
    if komorka[1] in ascii_uppercase:
        wspolrzendne.append((ascii_uppercase.index(komorka[0]) + 1) * 26)
        wspolrzendne[0] += ascii_uppercase.index(komorka[1])
        wiersz = komorka[2:]
        wspolrzendne.append(wiersz)
    else:
        wspolrzendne.append(ascii_uppercase.index(komorka[0]))
        wiersz = komorka[1:]
        wspolrzendne.append(int("".join(wiersz)) - 1)
    return wspolrzendne


def komorka_na_wspolrzendne2(adres: str) -> tuple[int, int]:
    adres = list(adres)
    komorka = [0, ""]
    for i in range(len(adres) - 1, -1, -1):
        if adres[i] in ascii_uppercase:
            komorka[0] += (ascii_uppercase.index(adres[i]) + 1) * 26**i
        else:
            komorka[1] += adres[i]
    komorka[1] = int(komorka[1][::-1]) - 1
    if komorka[0] > 0:
        komorka[0] -= 1
    return komorka


assert komorka_na_wspolrzedne("A12") == [0, 11]
assert komorka_na_wspolrzedne("A1") == [0, 0]

assert komorka_na_wspolrzendne2("A12") == [0, 11]
assert komorka_na_wspolrzendne2("A1") == [0, 0]
assert komorka_na_wspolrzendne2("AA1") == [26, 0]


def para_na_komorki(para: str) -> tuple[str, str]:
    wyjscie = ""
    wyjscie = tuple(para.split(":"))
    return wyjscie


print(zapelnianie_macierzy("A1:C2 A2:F2 B2:F4 E1:F4"))

assert para_na_komorki("A1:C2") == ("A1", "C2")


# assert odszyfrowanie_pozycji("A1:C2") == [[0, 0], [1, 2]]
assert arkusz("A1:C2 A2:F2 B2:F4 E1:F4") == 21
