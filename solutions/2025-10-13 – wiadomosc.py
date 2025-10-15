kod = list(map(str, "# 92 44 64 75 63 22 12 21 01 21 21".split()))
alfabet = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
haslo = ""
aktualny_znak = []
aktualny_znak_rozszyfrowany = ""
for i in range(0, len(kod)):  # 92 44 72
    znak_specjalny = False
    if kod[i] == "#":
        haslo = haslo + "#"
        znak_specjalny = True
        continue
    elif kod[i] == "*":
        haslo = haslo + "*"
        znak_specjalny = True
        continue
    kod[i] = int(kod[i])
    aktualny_znak = [kod[i] // 10, kod[i] % 10]
    if aktualny_znak[0] == 1 and aktualny_znak[1] == 2:
        haslo = haslo + " "
        znak_specjalny = True
    elif aktualny_znak[0] == 0 and aktualny_znak[1] == 2:
        haslo = haslo + "+"
        znak_specjalny = True

    if aktualny_znak[1] == 1 and znak_specjalny == False:
        haslo = haslo + str(aktualny_znak[0])
    elif aktualny_znak[0] < 9 and znak_specjalny == False:
        aktualny_znak_rozszyfrowany = alfabet[
            (aktualny_znak[0] - 2) * 3 + aktualny_znak[1] - 2
        ]
        haslo = haslo + aktualny_znak_rozszyfrowany
    elif znak_specjalny == False:
        aktualny_znak_rozszyfrowany = alfabet[
            (aktualny_znak[0] - 2) * 3 + aktualny_znak[1] - 1
        ]
        haslo = haslo + aktualny_znak_rozszyfrowany
print(haslo)


# aktualny_znak = "92"
# assert aktualny_znak[0] == "9"
# assert aktualny_znak[1] == "2"
# 92 44 64 75 63 22 12 21 01 21 21

klawiatura = ["0+", "1 ", "2abc", "3def"]
