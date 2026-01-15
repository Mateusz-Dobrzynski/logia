from string import ascii_lowercase


def harcerski(wejscie: str) -> str:
    # znajdujemy słowo w kolejności alfabetycznej
    # Sprawdzamy jego wagę
    # dopisujemy lub nie do wyjscia
    licznik_szukany, mianownik_szukany = wejscie.splitk
    for pierwsza_litera in ascii_lowercase:
        for druga_litera in ascii_lowercase:
            for trzecia_lietra in ascii_lowercase:
                slowo = pierwsza_litera + druga_litera + trzecia_lietra
                licznik_slowa, mianownik_slowa = liczenie_wagi_slowa(slowo)


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
assert liczenie_wagi_litery("n") == (3, 5)
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


print(ascii_lowercase)
assert harcerski("3 3") == "gqq lll qgq qqg qqr qrq rqq vvx vww vxv wvw wwv xvv"
