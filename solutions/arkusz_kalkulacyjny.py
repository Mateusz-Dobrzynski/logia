from string import ascii_uppercase

# macierz = [["" for _ in range()] for _ in range()]


def odszyfrowanie_pozycji(wejscie: str):
    odszyfrowane = []
    wejscie = wejscie.split(" ")
    zaszyfrowane_pary = []
    for i in range(len(wejscie)):
        zaszyfrowane_pary.append(wejscie[i].split(":"))
    for i in range(len(zaszyfrowane_pary)):
        kolumna = []
        wiersz = []
        obecna_para = zaszyfrowane_pary[i]
        for j in range(len(zaszyfrowane_pary[i])):
            for character in obecna_para[j]:
                if character in ascii_uppercase:
                    kolumna.append(character)
                else:
                    wiersz.append(character)
        wiersz = int("".join(wiersz))
        wiersz -= 1
        odszyfrowane.append(wiersz)
        if len(kolumna) == 2:
            odszyfrowane[i].append((ascii_uppercase.index(kolumna[0]) + 1) * 26)
            odszyfrowane[i][1] += ascii_uppercase.index(kolumna[1])
        else:
            odszyfrowane[i].append(ascii_uppercase.index(kolumna[0]))
    return odszyfrowane


def komorka_na_wspolrzedne(adres: str) -> tuple[int, int]:
    pass


assert komorka_na_wspolrzedne("A1") == (0, 0)


def para_na_komorki(para: str) -> tuple[str, str]:
    pass


assert para_na_komorki("A1:C2") == ("A1", "C2")


assert odszyfrowanie_pozycji("A1:C2") == [[0, 0], [1, 2]]
# assert arkusz("A1:C2 A2:F2 B2:F4 E1:F4") == 21
