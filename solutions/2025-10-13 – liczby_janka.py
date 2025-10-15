from math import *


def liczby(liczba: int):
    # iterujemy (sic!) po liczbach większych niż liczba bazowa
    # czy liczba jest złożona
    # średnia dzielników
    # pierwiastek z liczby
    # jeśli warunki są spełnione, dopisujemy do listy
    liczby_wyjsciowe = []
    if srednia_dzielnikow(liczba) == inf:
        print("nie da sie z tą liczbą!")
    liczba += 1
    while len(liczby_wyjsciowe) < 5:
        wynik_sredniej_dzielnikow = srednia_dzielnikow(liczba)
        if wynik_sredniej_dzielnikow <= sqrt(liczba):
            liczby_wyjsciowe.append(liczba)
        liczba += 1
    return " ".join(map(str, liczby_wyjsciowe))


def srednia_dzielnikow(liczba: int) -> float:
    dzielniki = [1]
    suma = 0
    for i in range(2, liczba // 2 + 1):
        if liczba % i == 0:
            dzielniki.append(i)
            suma += i
        if i == floor(sqrt(liczba)) and len(dzielniki) == 1:
            return inf
    srednia = suma / len(dzielniki)
    return srednia


def test_liczby():
    assert liczby(40) == "45 49 51 55 65"


test_dzielniki()
