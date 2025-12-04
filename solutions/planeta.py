class Dom:
    wsporzedna_x: int
    wsporzedna_y: int

    def podaj_wspolrzedne(self):
        return [self.wsporzedna_x, self.wsporzedna_y]


class Osiedle:
    domy: list[Dom]

    def wspolrzedne_domow(self):
        for dom in self.domy:
            print(dom.podaj_wspolrzedne())


d1 = Dom()
d1.wsporzedna_x = 15
d1.wsporzedna_y = 20

assert d1.podaj_wspolrzedne() == [15, 20]


# assert planeta(12, [[3,1], [1,1], [1,3], [2,12], [9,5], [8,6]]) == 4
