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


def robienie_macierzy(zaszyfrowana_wiadomosc, szerokosc):
    tablica = [[] for _ in range(szerokosc)]
    for i in range(szerokosc):
        for j in range(szerokosc):
            tablica[i].append(zaszyfrowana_wiadomosc[i * szerokosc + j])
    return tablica


def podaj_litere(szukana_pozycja, tablica):
    wiersz = szukana_pozycja // len(tablica)
    kolumna = szukana_pozycja % len(tablica)
    return tablica[wiersz][kolumna - 1]


def obracanie(tablica):
    obrucona_tablica = [[[] for _ in range(len(tablica))] for _ in range(len(tablica))]
    for i in range(len(tablica)):
        for j in range(len(tablica)):
            obrucona_tablica[i][j] = tablica[j][len(tablica) - i - 1]
    return obrucona_tablica


assert podaj_litere(4, tablica_testowa) == "i"
assert (
    odszyfruj("6\n1 4 8 12 15 20 23 30 34\ncxrizboeaxwkdwaaajwwgnasikzlezoy.afa")
    == "ciekawazabawawszyfrowanie"
)
assert robienie_macierzy("cxrizboeaxwkdwaaajwwgnasikzlezoy.afa", 6) == tablica_testowa

assert obracanie([[1, 2], [3, 4]]) == [[2, 4], [1, 3]]
