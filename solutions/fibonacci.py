def liczenie(liczba_dziesietna):
    if liczba_dziesietna == 0:
        return "0"
    fibonacci = ciag_fibonacciego(liczba_dziesietna)
    if fibonacci[-1] > liczba_dziesietna:
        fibonacci.pop()
    wynik = ""
    while len(fibonacci) > 0:
        if fibonacci[-1] <= liczba_dziesietna:
            wynik += "1"
            liczba_dziesietna -= fibonacci[-1]
        else:
            wynik += "0"
        fibonacci.pop()
    return wynik


def ciag_fibonacciego(liczba_dziesietna):
    i = 1
    fibonacci = [1, 2]
    while fibonacci[i] < liczba_dziesietna:
        fibonacci.append(fibonacci[i - 1] + fibonacci[i])
        i += 1
    return fibonacci


assert ciag_fibonacciego(3) == [1, 2, 3]
assert ciag_fibonacciego(4) == [1, 2, 3, 5]

assert liczenie(0) == "0"
assert liczenie(1) == "1"
assert liczenie(2) == "10"
assert liczenie(3) == "100"
assert liczenie(4) == "101"
