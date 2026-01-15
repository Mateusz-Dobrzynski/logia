def znajdz_wyraz(wejscie: str) -> int:
    tabela, slowo = wejscie.split("\n")
    for i in range(len(tabela)):
        if tabela[i] == slowo[0]:
            odwidzone_pozycje = [i]
            if szukanie_slowa(tabela, slowo, odwidzone_pozycje) == True:
                return i + 1
    return -1


# funkcja sprawdzająca sąsiadów
def sasiedzi(tabela: str, pozycja_litery: int) -> list[int]:
    litery_sasiadujace = []
    if (pozycja_litery - 10) >= 0:
        litery_sasiadujace.append(pozycja_litery - 10)
    if (pozycja_litery + 10) < 100:
        litery_sasiadujace.append(pozycja_litery + 10)
    if pozycja_litery % 10 != 9:
        litery_sasiadujace.append(pozycja_litery + 1)
    if pozycja_litery % 10 != 0:
        litery_sasiadujace.append(pozycja_litery - 1)
    return litery_sasiadujace


def szukanie_slowa(tabela: str, slowo: str, odwiedzone_pozycje: list[int]) -> bool:
    if len(slowo) == 0:
        return True
    pozycja_poczatkowa = odwiedzone_pozycje[-1]
    if tabela[pozycja_poczatkowa] != slowo[0]:
        return False
    else:
        for sasiad in sasiedzi(tabela, pozycja_poczatkowa):
            if sasiad in odwiedzone_pozycje:
                continue
            odwiedzone_pozycje.append(sasiad)
            if szukanie_slowa(tabela, slowo[1:], odwiedzone_pozycje) == True:
                return True
        return False


assert (
    znajdz_wyraz(
        "ABCDERASSQMGYUKAESSQTRWOISOABCUIHKAIWYUKYEWAGHOSSQRTTKRAKYUKWYUKAYUKSQISSQASSQUKEYYUKYUKSQOSASQAQYUK\nKRAKOWIAK"
    )
    == 54
)
