def sito(gora):
    liczby_zlozone = []
    liczby_pierwsze = []
    liczba_liczona = 2
    while liczba_liczona <= gora:
        liczby_pierwsze.append(liczba_liczona)
        liczba_liczona_zmienna = liczba_liczona
        while liczba_liczona_zmienna < gora:
            liczba_liczona_zmienna += liczba_liczona
            liczby_zlozone.append(liczba_liczona_zmienna)
        liczba_liczona += 1
        while liczba_liczona in liczby_zlozone:
            liczba_liczona += 1
    return liczby_pierwsze


def germain(min, gora):
    liczby_pierwsze = sito(gora * 2 + 1)
    liczby_pierwsze_ponad = []
    liczby_germain = 0
    while liczby_pierwsze[0] < min:
        liczby_pierwsze.pop(0)
    while liczby_pierwsze[-1] > gora:
        liczby_pierwsze_ponad.append(liczby_pierwsze.pop(-1))
    for liczba_pierwsza in liczby_pierwsze:
        liczba_pierwsza = liczba_pierwsza * 2 + 1
        if (
            liczba_pierwsza in liczby_pierwsze_ponad
            or liczba_pierwsza in liczby_pierwsze
        ):
            liczby_germain += 1
    return liczby_germain


assert sito(10) == [2, 3, 5, 7]
assert sito(13) == [2, 3, 5, 7, 11, 13]
assert germain(10, 1000) == 34
