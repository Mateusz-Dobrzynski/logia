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
    tablica = robienie_macierzy(zaszyfrowana_wiadomosc, szerokosc)
    odszyfrowana_wiadomosc = ""
    pozycje = (pozycje).split(" ")
    for _ in range(4):
        for i in range(len(pozycje)):
            odszyfrowana_wiadomosc += podaj_litere(int(pozycje[i]), tablica)
        tablica = obracanie(tablica)
    return odszyfrowana_wiadomosc


def robienie_szablonu(pozycje: list, szerokosc: int) -> list[list[bool]]:
    szablon = [[False for _ in range(szerokosc)] for _ in range(szerokosc)]
    for i in range(len(pozycje)):
        szukana_pozycja = pozycje[i] - 1
        wiersz = szukana_pozycja // szerokosc
        kolumna = szukana_pozycja % szerokosc
        szablon[wiersz][kolumna] = True
    return szablon


def przykladanie_szablonu(szablon, tablica) -> str:
    pass


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
    == "ciekawazabawawszyfrowanie.afa"
)
assert robienie_macierzy("cxrizboeaxwkdwaaajwwgnasikzlezoy.afa", 6) == tablica_testowa

assert obracanie([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]
