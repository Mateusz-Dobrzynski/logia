def palindrom(text: str):
    palindrom = ""
    srodek = ""
    lewa_polowa = ""
    prawa_polowa = ""
    letters = list(text)
    letters.sort()
    i = 1
    while i < len(letters):
        prawa_litera = letters[i]
        lewa_litera = letters[i - 1]
        if lewa_litera == prawa_litera:
            prawa_polowa = prawa_litera + prawa_polowa
            lewa_polowa = lewa_polowa + lewa_litera
            i += 1
        elif srodek == "":
            srodek = lewa_litera
        i += 1
    palindrom = lewa_polowa + srodek + prawa_polowa
    print(palindrom)
    return palindrom


def test_palindrom():
    assert palindrom("kajak") == "akjka"


test_palindrom()
