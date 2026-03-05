# https://logia.oeiizk.waw.pl/strony/bankzadan/L21_e3_zad2.pdf

from string import ascii_lowercase


def harcerski(wejscie: str) -> str:
    licznik_szukany, mianownik_szukany = wejscie.split(" ")
    slowa_spelniajace = []
    for pierwsza_litera in ascii_lowercase:
        for druga_litera in ascii_lowercase:
            for trzecia_lietra in ascii_lowercase:
                slowo = pierwsza_litera + druga_litera + trzecia_lietra
                licznik_slowa, mianownik_slowa = liczenie_wagi_slowa(slowo)
                if czy_rowny(
                    licznik_slowa, mianownik_slowa, licznik_szukany, mianownik_szukany
                ):
                    slowa_spelniajace.append(slowo)
    wynik = " ".join(slowa_spelniajace)
    return wynik


def liczenie_wagi_litery(litera):
    alfabet = ["abcdef", "ghijk", "lmnop", "qrstu", "vwxyz"]
    licznik = 0
    mianownik = 0
    for i in range(len(alfabet)):
        if litera in alfabet[i]:
            mianownik = i + 1
            licznik = (alfabet[i].index(litera)) + 1
    return licznik, mianownik


assert liczenie_wagi_litery("a") == (1, 1)
assert liczenie_wagi_litery("g") == (1, 2)
assert liczenie_wagi_litery("n") == (3, 3)
assert liczenie_wagi_litery("u") == (5, 4)
assert liczenie_wagi_litery("z") == (5, 5)


def liczenie_wagi_slowa(slowo):
    licznik_slowa = 0
    mianownik_slowa = 1
    for litera in slowo:
        licznik_litery, mianownik_litery = liczenie_wagi_litery(litera)
        licznik_slowa, mianownik_slowa = dodawanie_ulamkow_zwyklych(
            licznik_litery,
            mianownik_litery,
            licznik_slowa,
            mianownik_slowa,
        )
    return licznik_slowa, mianownik_slowa


def dodawanie_ulamkow_zwyklych(
    licznik1, mianownik1, licznik2, mianownik2
) -> tuple[int, int]:
    licznik1 *= mianownik2
    licznik2 *= mianownik1
    return licznik1 + licznik2, mianownik1 * mianownik2


def czy_rowny(licznik1, mianownik1, licznik2, mianownik2):
    if mianownik1 == mianownik2:
        if licznik1 == licznik2:
            return True
        return False
    licznik1 *= mianownik2
    licznik2 *= mianownik1
    if licznik1 == licznik2:
        return True
    return False


assert czy_rowny(1, 2, 4, 8)
assert not czy_rowny(1, 5, 3, 7)

assert harcerski("3 3") == "gqq lll qgq qqg qqr qrq rqq vvx vww vxv wvw wwv xvv"
