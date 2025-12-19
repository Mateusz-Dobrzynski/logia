# odbicie lustrzane
# obliczyć przesunięcie z klucza
# przesunąć odbite litery
from string import ascii_lowercase


def odbicie_lustrzane(litera: str) -> str:
    pozycja_litery = ascii_lowercase.index(litera)
    if pozycja_litery > 13:
        pozycja_litery -= 13
        pozycja_litery_koniec = 13 - pozycja_litery
        lustrzana_litera = ascii_lowercase[pozycja_litery_koniec - 1]
    else:
        lustrzana_litera = ascii_lowercase[-(pozycja_litery + 1)]
    return lustrzana_litera


def szyfr(wejscie: str):
    szyfrogram = ""
    slowo, klucz = wejscie.split(" ")
    if len(klucz) < len(slowo):
        roznica = len(slowo) - len(klucz)
        for i in range(roznica):
            klucz += klucz[i]
    for i in range(len(slowo)):
        litera = slowo[i]
        odbita_litera = odbicie_lustrzane(litera)
        przesunieta_litera = przesuniecie(odbita_litera, klucz[i])
        szyfrogram += przesunieta_litera
    return szyfrogram


def przesuniecie(litera: str, litera_klucz: str) -> str:
    liczba_klucz = ascii_lowercase.index(litera_klucz)
    index_litery = ascii_lowercase.index(litera)
    if index_litery + liczba_klucz > 25:
        index_przesunieta = (index_litery + liczba_klucz) - 25
        przesunieta_litera = ascii_lowercase[index_przesunieta]
    else:
        index_przesunieta = index_litery + liczba_klucz + 1
        if index_przesunieta > 25:
            index_przesunieta -= 26
        przesunieta_litera = ascii_lowercase[index_przesunieta]
    return przesunieta_litera


assert szyfr("konkurs logia") == "batyguw"

assert przesuniecie("p", "l") == "b"
assert przesuniecie("l", "o") == "a"
assert przesuniecie("m", "g") == "t"
assert przesuniecie("p", "i") == "y"
assert przesuniecie("f", "a") == "g"
assert przesuniecie("i", "l") == "u"

assert odbicie_lustrzane("z") == "a"
assert odbicie_lustrzane("y") == "b"

assert odbicie_lustrzane("a") == "z"
assert odbicie_lustrzane("b") == "y"
