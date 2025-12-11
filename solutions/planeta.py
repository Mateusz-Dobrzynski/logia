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


d1 = Dom()
d1.wsporzedna_x = 15
d1.wsporzedna_y = 20

assert d1.podaj_wspolrzedne() == [15, 20]


def liczenie_odleglosci(d1: Dom, d2: Dom, rozmiar: int):
    odleglosc_x = abs(d1.wsporzedna_x - d2.wsporzedna_x)
    if odleglosc_x > rozmiar / 2:
        odleglosc_x -= rozmiar
    odleglosc_y = abs(d1.wsporzedna_y - d2.wsporzedna_y)
    if odleglosc_y > rozmiar / 2:
        odleglosc_y -= rozmiar
    return odleglosc_x + odleglosc_y


def odl(a, b, r):
    x = abs(a[0] - b[0])
    if x > r / 2:
        x = r - x
    y = abs(a[1] - b[1])
    if y > r / 2:
        y = r - y
    return x + y


def osiedle(domy: list[Dom], rozmiar):
    aktulnie_sprawdzany_dom = domy[0]
    sasiadujace_domy = set(sasiedzi(aktulnie_sprawdzany_dom, domy, rozmiar))

    for aktulnie_sprawdzany_dom in sasiadujace_domy:
        while len(sasiedzi(aktulnie_sprawdzany_dom, domy, rozmiar)) - 1 > 0:
            sasiadujace_domy.union(sasiedzi(aktulnie_sprawdzany_dom, domy, rozmiar))
    return len(sasiadujace_domy)


print(odl([1, 4], [8, 9], 10))


def planeta(wejscie):
    domy = wejscie[1]


# assert planeta(12, [[3,1], [1,1], [1,3], [2,12], [9,5], [8,6]]) == 4
