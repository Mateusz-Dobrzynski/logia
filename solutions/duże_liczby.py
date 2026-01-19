def liczba(liczba_maksymalna, potega) -> int:
    liczba_szukana = liczba_maksymalna ** (1 / potega) // 1
    return liczba_szukana


def czy_spelnia_warunek(liczba_bez_potegi, liczba_maksymalna, potega):
    if liczba_bez_potegi**potega <= liczba_maksymalna:
        return True
    return False


def liczba2(liczba_maksymalna, potega):
    liczba_minimalna = 0
    liczba_maksymalna_kopia = liczba_maksymalna
    polowa = 0
    while liczba_minimalna < liczba_maksymalna:
        polowa = (liczba_maksymalna + liczba_minimalna) // 2
        if czy_spelnia_warunek(polowa, liczba_maksymalna_kopia, potega):
            liczba_minimalna = polowa + 1
        else:
            liczba_maksymalna = polowa
    return polowa - 1


assert 2**3 == 8
assert 8 ** (1 / 3) == 2

assert liczba2(1024, 2) == 32
assert liczba2(121104, 2) == 348
assert liczba2(9795241251741333007812600000000000000, 7) == 192500
assert (
    liczba2(90972061672647417382949994702882855264900000, 2) == 9537927535510396054172
)
