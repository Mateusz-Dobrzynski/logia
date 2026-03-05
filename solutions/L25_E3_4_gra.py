MACIERZ_TESTOWA = [
    ["M", "S", "S", "X"],
    ["S", "X", "X", "S"],
    ["S", "S", "X", "S"],
    ["X", "S", "S", "J"],
]


def gra(wejscie: str) -> str:
    # tablica
    # liczenie przejścia małgosi do jasia
    # odwrócić połowę ścieżki
    # wypisać wynik
    lista_krokow, odwiedzone_pozycje = liczenie(robienie_macierzy(wejscie), wejscie)
    if lista_krokow == "BRAK":
        print("BRAK")
        return ""
    lista_krokow = usuwanie_slepych_zaulkow(lista_krokow, odwiedzone_pozycje)
    malgosia, jas = odwarcanie_polowy_scierzki(lista_krokow)
    wynik = f"{malgosia}\n{jas}"
    return wynik


def test_zaulkow():
    lista, odwiedzone = liczenie(MACIERZ_TESTOWA, "MSSXSXXSSSXSXSSJ")
    usuwanie_slepych_zaulkow(lista, odwiedzone)
    return


def czy_sasiaduja(punkt1, punkt2):
    if abs(punkt1[0] - punkt2[0]) > 1:
        return False
    if abs(punkt1[1] - punkt2[1]) > 1:
        return False
    if abs(punkt1[1] - punkt2[1]) == 1 and abs(punkt1[0] - punkt2[0]) == 1:
        return False
    return True


def usuwanie_slepych_zaulkow(
    kroki: str, odwiedzione_pozycje: list[tuple[int, int]]
) -> str:
    lista_krokow = list(kroki)
    for i in range(len(lista_krokow) - 1, 1, -1):
        if czy_sasiaduja(odwiedzione_pozycje[i], odwiedzione_pozycje[i - 1]) == False:
            j = i
            while (
                czy_sasiaduja(odwiedzione_pozycje[j], odwiedzione_pozycje[j - 1])
                == False
            ):
                odwiedzione_pozycje.pop(j - 1)
                lista_krokow.pop(j)
                j -= 1
    return "".join(lista_krokow)


def robienie_macierzy(wejscie: str):
    szerokosc = int(len(wejscie) ** 0.5)
    macierz = [["" for _ in range(szerokosc)] for _ in range(szerokosc)]
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            macierz[i][j] = wejscie[i * szerokosc + j]
    return macierz


def odwarcanie_polowy_scierzki(scierzka):
    dlugosc_scierzki_malgosia = len(scierzka)
    dlugosc_scierzki_malgosia = dlugosc_scierzki_malgosia // 2
    if len(scierzka) % 2 == 0:
        dlugosc_scierzki_jas = dlugosc_scierzki_malgosia
    else:
        dlugosc_scierzki_jas = dlugosc_scierzki_malgosia + 1
        dlugosc_scierzki_malgosia += 1
    malgosia = scierzka[0:dlugosc_scierzki_malgosia]
    jas = list(scierzka[dlugosc_scierzki_jas : len(scierzka)])
    jas.reverse()
    jas = "".join(jas)
    jas = jas.translate(str.maketrans("DGLP", "GDPL"))
    return malgosia, jas


def szukanie_litery(wejscie, szukana_litera):
    szerokosc = int(len(wejscie) ** 0.5)
    litera_poz = wejscie.index(szukana_litera)
    wiersz = litera_poz // szerokosc
    kolumna = litera_poz % szerokosc
    return wiersz, kolumna


def liczenie(macierz: list[list[str]], wejscie):
    start_wiersz, start_kolumna = szukanie_litery(wejscie, "M")
    koniec = szukanie_litery(wejscie, "J")
    pozycja_wiersz = start_wiersz
    pozycja_kolumna = start_kolumna
    kroki = ""
    odwiedzone_pozycje = []
    droga = False
    mozliwe_ruchy = []
    while droga == False:
        odwiedzone_pozycje.append((pozycja_wiersz, pozycja_kolumna))
        if pozycja_wiersz - 1 != -1:
            if (
                macierz[pozycja_wiersz - 1][pozycja_kolumna] in ["S", "J"]
                and (pozycja_wiersz - 1, pozycja_kolumna) not in odwiedzone_pozycje
            ):
                mozliwe_ruchy.append((pozycja_wiersz - 1, pozycja_kolumna, "G"))
        if pozycja_kolumna - 1 != -1:
            if (
                macierz[pozycja_wiersz][pozycja_kolumna - 1] in ["S", "J"]
                and (pozycja_wiersz, pozycja_kolumna - 1) not in odwiedzone_pozycje
            ):
                mozliwe_ruchy.append((pozycja_wiersz, pozycja_kolumna - 1, "L"))
        if pozycja_kolumna + 1 != len(macierz[0]):
            if (
                macierz[pozycja_wiersz][pozycja_kolumna + 1] in ["S", "J"]
                and (pozycja_wiersz, pozycja_kolumna + 1) not in odwiedzone_pozycje
            ):
                mozliwe_ruchy.append((pozycja_wiersz, pozycja_kolumna + 1, "P"))
        if pozycja_wiersz + 1 != len(macierz[0]):
            if (
                macierz[pozycja_wiersz + 1][pozycja_kolumna] in ["S", "J"]
                and (pozycja_wiersz + 1, pozycja_kolumna) not in odwiedzone_pozycje
            ):
                mozliwe_ruchy.append((pozycja_wiersz + 1, pozycja_kolumna, "D"))
        if len(mozliwe_ruchy) == 0:
            return "BRAK"
        robocza = mozliwe_ruchy.pop()
        kroki += robocza[2]
        pozycja_wiersz = robocza[0]
        pozycja_kolumna = robocza[1]
        if (pozycja_wiersz, pozycja_kolumna) == koniec:
            droga = True
    return kroki, odwiedzone_pozycje


assert szukanie_litery("MXSXSXXSSSXSXSJX", "M") == (0, 0)
assert szukanie_litery("MSXJ", "J") == (1, 1)
assert robienie_macierzy("XXSS") == [["X", "X"], ["S", "S"]]

assert odwarcanie_polowy_scierzki("GDPDLP") == ("GDP", "LPG")
assert odwarcanie_polowy_scierzki("GDPDLPL") == ("GDPD", "PLP")

assert czy_sasiaduja((0, 1), (0, 2)) == True
assert czy_sasiaduja((1, 0), (2, 0)) == True
assert czy_sasiaduja((1, 0), (2, 1)) == False

test_zaulkow()
