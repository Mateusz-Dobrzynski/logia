samogloski = ["a", "e", "i", "o", "u", "y", "ą", "ę"]


def waga_slowa(slowo, samogloski):
    slowo = list(slowo)
    waga = 0
    if len(slowo) % 2 == 0:
        poczatek_slowa = slowo[0 : len(slowo) // 2]
        koniec_slowa = slowo[len(slowo) // 2 :]
        for i in range(len(slowo) // 2):
            if poczatek_slowa[i] in samogloski:
                waga += i
            else:
                waga += i + 2
            if koniec_slowa[-(i)] in samogloski:
                waga += i
            else:
                waga += i + 2
    else:
        poczatek_slowa = slowo[0 : len(slowo) // 2]
        srodek_slowa = slowo[(len(slowo) // 2)]
        koniec_slowa = slowo[len(slowo) // 2 :]
        for i in range(len(poczatek_slowa)):
            if poczatek_slowa[i] in samogloski:
                waga += i
            else:
                waga += i + 2
            if koniec_slowa[-1 - i] in samogloski:
                waga += i
            else:
                waga += i + 2
            k = i
        if srodek_slowa in samogloski:
            waga += k
        else:
            waga += k + 3
    return waga


def ukladanie_alfabetycznie(slowa):
    slowa = sorted(slowa)
    return slowa


def uporzadkowane(wejscie):
    wejscie = list(wejscie)
    uporzadkowane_slowa = ""


#    for i in range(len(wejscie)):

waga = waga_slowa("ala", ["a", "e", "i", "o", "u", "y", "ą", "ę"])

assert waga_slowa("ala", ["a", "e", "i", "o", "u", "y", "ą", "ę"]) == 3
assert waga_slowa("kota", ["a", "e", "i", "o", "u", "y", "ą", "ę"]) == 6
# assert uporzadkowane("ala ma kota")== "ma ala kota "
