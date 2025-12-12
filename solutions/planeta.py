class Dom:
    wsporzedna_x: int
    wsporzedna_y: int

    def __init__(self, x: int, y: int) -> None:
        self.wsporzedna_x = x
        self.wsporzedna_y = y

    def podaj_wspolrzedne(self):
        return [self.wsporzedna_x, self.wsporzedna_y]


def sasiedzi(dom: Dom, domy: list[Dom], rozmiar):
    sasiadzi = []
    for i in range(len(domy)):
        if liczenie_odleglosci(dom, domy[i], rozmiar) < 5:
            sasiadzi.append(domy[i])
    return sasiadzi


class Osiedle:
    domy: list[Dom]

    def wspolrzedne_domow(self):
        for dom in self.domy:
            print(dom.podaj_wspolrzedne())


def liczenie_odleglosci(d1: Dom, d2: Dom, rozmiar: int):
    odleglosc_x = abs(d1.wsporzedna_x - d2.wsporzedna_x)
    if odleglosc_x > rozmiar / 2:
        odleglosc_x -= rozmiar
    odleglosc_y = abs(d1.wsporzedna_y - d2.wsporzedna_y)
    if odleglosc_y > rozmiar / 2:
        odleglosc_y -= rozmiar
    return abs(odleglosc_x) + abs(odleglosc_y)


def rozmiar_osiedla(domy: list[Dom], rozmiar, dom_poczatkowy: Dom):
    aktulnie_sprawdzany_dom = dom_poczatkowy
    sasiadujace_domy = set(sasiedzi(aktulnie_sprawdzany_dom, domy, rozmiar))
    sprawdzone_domy = []

    for aktulnie_sprawdzany_dom in sasiadujace_domy:
        if aktulnie_sprawdzany_dom not in sprawdzone_domy:
            sprawdzone_domy.append(aktulnie_sprawdzany_dom)
            sasiadujace_domy.union(sasiedzi(aktulnie_sprawdzany_dom, domy, rozmiar))
    return len(sasiadujace_domy)


# assert (
#     rozmiar_osiedla(
#         [Dom(5, 6), Dom(6, 6), Dom(5, 7), Dom(9, 2), Dom(10, 2)], 10, Dom(6, 6)
#     )
#     == 3
# )


# print(odl([1, 4], [8, 9], 10))


def planeta(rozmiar_planety: int, lista_wspolrzednych: list[list[int]]):
    domy = buduj_domy(lista_wspolrzednych)
    rozmiar_najwiekszego_osiedla = 0
    for i in range(len(domy)):
        if (
            rozmiar_osiedla(domy, rozmiar_planety, domy[i])
            > rozmiar_najwiekszego_osiedla
        ):
            rozmiar_najwiekszego_osiedla = rozmiar_osiedla(
                domy, rozmiar_planety, domy[i]
            )
    return rozmiar_najwiekszego_osiedla


def buduj_domy(lista_wspolrzednych: list[list[int]]) -> list[Dom]:
    domy = []
    for i in range(len(lista_wspolrzednych)):
        x = lista_wspolrzednych[i][0]
        y = lista_wspolrzednych[i][1]
        domy.append(Dom(x, y))
    return domy


assert planeta(12, [[3, 1], [1, 1], [1, 3], [2, 12], [9, 5], [8, 6]]) == 4

assert liczenie_odleglosci(Dom(3, 1), Dom(8, 5), 12) > 5
assert liczenie_odleglosci(Dom(1, 1), Dom(8, 5), 12) > 5
assert liczenie_odleglosci(Dom(3, 3), Dom(8, 5), 12) > 5
assert liczenie_odleglosci(Dom(2, 12), Dom(8, 5), 12) > 5


assert liczenie_odleglosci(Dom(9, 5), Dom(3, 1), 12) > 5
