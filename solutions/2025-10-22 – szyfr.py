tablica_testowa = [
    ["c", "x", "r", "i", "z", "b"],
    ["o", "e", "a", "x", "w", "k"],
    ["d", "w", "a", "a", "a", "j"],
    ["w", "w", "g", "n", "a", "s"],
    ["i", "k", "z", "l", "e", "z"],
    ["o", "y", ".", "a", "f", "a"],
]


def odszyfruj(wejscie: str) -> str:
    szerokosc, pozycje, zaszyfrowana_wiadomosc = wejscie.split("\n")
    szerokosc = int(szerokosc)
    rozmiar_macierzy = szerokosc * szerokosc
    liczba_tablic = int(len(zaszyfrowana_wiadomosc) // rozmiar_macierzy)
    odszyfrowana_wiadomosc = ""
    pozycje = pozycje.split(" ")
    for i in range(liczba_tablic):
        fragment_szyfrogramu = zaszyfrowana_wiadomosc[
            i * rozmiar_macierzy : i * rozmiar_macierzy + rozmiar_macierzy
        ]
        tablica = robienie_macierzy(fragment_szyfrogramu, szerokosc)
        szablon = robienie_szablonu(pozycje, szerokosc)
        for _ in range(4):
            odszyfrowana_wiadomosc = przykladanie_szablonu(
                szablon, tablica, odszyfrowana_wiadomosc
            )
            szablon = obracanie(szablon)
    return odszyfrowana_wiadomosc.split(".")[0]


def robienie_szablonu(pozycje: list[str], szerokosc: int) -> list[list[bool]]:
    szablon = [[False for _ in range(szerokosc)] for _ in range(szerokosc)]
    for i in range(len(pozycje)):
        szukana_pozycja = int(pozycje[i]) - 1
        wiersz = szukana_pozycja // szerokosc
        kolumna = szukana_pozycja % szerokosc
        szablon[wiersz][kolumna] = True
    return szablon


def przykladanie_szablonu(szablon, tablica, odszyfrowana_wiadomosc) -> str:
    for i in range(len(tablica)):
        for j in range(len(tablica)):
            if szablon[i][j] == True:
                odszyfrowana_wiadomosc += tablica[i][j]
    return odszyfrowana_wiadomosc


def obracanie_szablonu(szablon):
    obrucony_szablon = [[[] for _ in range(len(szablon))] for _ in range(len(szablon))]
    for i in range(len(szablon)):
        for j in range(len(szablon)):
            obrucony_szablon[j][len(szablon) - i] = szablon[i][j]
    return obrucony_szablon


def robienie_macierzy(zaszyfrowana_wiadomosc, szerokosc):
    szerokosc = int(szerokosc)
    tablica = [[] for _ in range(szerokosc)]
    for i in range(szerokosc):
        for j in range(szerokosc):
            tablica[i].append(zaszyfrowana_wiadomosc[i * szerokosc + j])
    return tablica


def podaj_litere(szukana_pozycja: int, tablica: list[list[str]]) -> str:
    szukana_pozycja -= 1
    wiersz = szukana_pozycja // len(tablica)
    kolumna = szukana_pozycja % len(tablica)
    litera = tablica[wiersz][kolumna]
    return litera


def obracanie(tablica) -> list[list]:
    obrucona_tablica = [[[] for _ in range(len(tablica))] for _ in range(len(tablica))]
    for i in range(len(tablica)):
        wiersz = tablica[i]
        for j in range(len(tablica)):
            komorka = wiersz[j]
            obrucona_tablica[j][len(tablica) - i - 1] = komorka
    return obrucona_tablica


obracanie(robienie_macierzy("cxrizboeaxwkdwaaajwwgnasikzlezoy.afa", 6))

assert podaj_litere(4, tablica_testowa) == "i"
assert (
    odszyfruj("6\n1 4 8 12 15 20 23 30 34\ncxrizboeaxwkdwaaajwwgnasikzlezoy.afa")
    == "ciekawazabawawszyfrowanie"
)
assert robienie_macierzy("cxrizboeaxwkdwaaajwwgnasikzlezoy.afa", 6) == tablica_testowa

assert obracanie([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]

assert (
    odszyfruj("4\n1 2 11 12\nalaaaiakloamatpsmaztsajaoikovp.f")
    == "alamakotaipsaalamakotaipsa"
)

assert (
    odszyfruj(
        "12\n1 2 3 4 5 6 13 14 15 16 17 18 25 26 27 28 29 30 37 38 39 40 41 42 49 50 51 52 53 54 61 62 63 64 65 66\ndotrzedotrzechrazychrazysztukasztukadotrzedotrzechrazychrazysztukasztukadotrzedotrzechrazychrazysztukasztukadotrzedotrzechrazychrazysztukasztukadotrzedotrzechrazychrazysztukasztukadotrzedotrzechrazychrazysztukasztukadotrzedotrzechrazychrazysztukasztukadotrzedotrzechrazychrazysztukasztukadotrzedotrzechrazychrazysztukasztukadotrzedotrzechrazychrazysztukasztukadotrzedotrzechrazychrazysztukasztuka.ontcpdotrzeesvnlxchrazygowbkdsztuka"
    )
    == "dotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztukadotrzechrazysztuka"
)
