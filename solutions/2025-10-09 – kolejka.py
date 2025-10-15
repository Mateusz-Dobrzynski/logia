def kolejka_liczenie(text: str):
    zmienna = text.split("\n")
    k = int(zmienna[0])
    kolejka = list(map(int, zmienna[1].split()))
    dlugosc = 0
    najkrotsza_dlugosc = 999999999999
    pierwsza_liczba_pozycja = 0
    k_kopia = k
    for i in range(0, len(kolejka)):
        k = k_kopia
        dlugosc = 0
        h = i
        koniec_liczb = False
        while k > 0 and not koniec_liczb:
            try:
                sprawdzana_liczba = kolejka[h]
            except:
                koniec_liczb = True
            if kolejka[i] == sprawdzana_liczba:
                k -= 1
            dlugosc += 1
            h += 1
        if najkrotsza_dlugosc > dlugosc and not koniec_liczb:
            najkrotsza_dlugosc = dlugosc
            pierwsza_liczba_pozycja = i + 1
    print(pierwsza_liczba_pozycja, najkrotsza_dlugosc)
    return f"{pierwsza_liczba_pozycja} {najkrotsza_dlugosc}"


def test():
    assert kolejka_liczenie("3\n2 3 1 2 1 3 1 1 2") == "5 4"


test()
