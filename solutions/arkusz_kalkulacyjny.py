from string import ascii_uppercase

# macierz = [["" for _ in range()] for _ in range()]


def robienie_macierzy(najwiekszy_wiersz, najwieka_kolumna):
    return [
        [False for _ in range(najwiekszy_wiersz + 1)]
        for _ in range(najwieka_kolumna + 1)
    ]


def odszyfrowanie_pozycji(wejscie: str):
    pary = wejscie.split(" ")
    najwieksza_kolumna = 0
    najwiekszy_wiersz = 0
    odszyfrowane = []
    for i in range(len(pary)):
        poczatek_zakresu, koniec_zakresu = para_na_komorki(pary[i])  # A1, C2
        wspolrzedne_poczatket = komorka_na_wspolrzedne(poczatek_zakresu)
        wspolrzedne_koniec = komorka_na_wspolrzedne(koniec_zakresu)
        odszyfrowane.append(wspolrzedne_poczatket)  # 00
        odszyfrowane.append(wspolrzedne_koniec)  # 21
        if wspolrzedne_koniec[0] > najwiekszy_wiersz:
            najwiekszy_wiersz = wspolrzedne_koniec[0]
        if wspolrzedne_koniec[1] > najwieksza_kolumna:
            najwieksza_kolumna = wspolrzedne_koniec[1]
    return odszyfrowane, najwiekszy_wiersz, najwieksza_kolumna


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


assert para_na_komorki("A1:C2") == ("A1", "C2")


# assert odszyfrowanie_pozycji("A1:C2") == [[0, 0], [1, 2]]
# assert arkusz("A1:C2 A2:F2 B2:F4 E1:F4") == 21
