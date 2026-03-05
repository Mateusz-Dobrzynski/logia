def czy_sfeniczna(liczba) -> bool:
    dzielniki = [1]
    aktualny_dzielnik = 1
    while len(dzielniki) < 9 and aktualny_dzielnik < liczba:
        aktualny_dzielnik += 1
        if liczba % (aktualny_dzielnik * aktualny_dzielnik) == 0:
            return False
        if liczba % aktualny_dzielnik == 0:
            dzielniki.append(aktualny_dzielnik)
    if len(dzielniki) == 8:
        return True
    return False


def sfeniczne(liczba):
    liczba = int(liczba)
    liczby_sfeniczne = ""
    while liczby_sfeniczne.count(" ") < 3:
        liczba += 1
        if czy_sfeniczna(liczba) == True:
            liczby_sfeniczne += " " + str(liczba)
    return liczby_sfeniczne.strip()


assert czy_sfeniczna(30) == True
assert czy_sfeniczna(31) == False
assert sfeniczne("12") == "30 42 66"
