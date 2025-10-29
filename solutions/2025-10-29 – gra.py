def gra(wejscie: str) -> str:
    # tablica
    # liczenie przejścia małgosi do jasia
    # odwrócić połowę ścieżki
    # wypisać wynik
    pass


def robienie_macierzy(wejscie: str):
    szerokosc = int(len(wejscie) ** 0.5)
    macierz = [["" for _ in range(szerokosc)] for _ in range(szerokosc)]
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            macierz[i][j] = wejscie[i * szerokosc + j]
    return macierz


assert robienie_macierzy("XXSS") == [["X", "X"], ["S", "S"]]

# assert gra("MXSXSXXSSSXSXSJX") == "DDP\nLG"
