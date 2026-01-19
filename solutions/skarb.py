# 2026-E02


komnaty = {
    "A": ["G", "B", "C"],
    "B": ["E", "D", "A"],
    "C": ["H", "A", "D"],
    "D": ["B", "F", "C"],
    "E": ["B", "G", "F"],
    "F": ["E", "H", "D"],
    "G": ["E", "A", "H"],
    "H": ["F", "G", "C"],
}


def gdzie_jest_skarb(lista_krokow: str) -> str:
    aktualna_pozycja = "A"
    poprzednia_komnata = "B"
    for i in range(len(lista_krokow)):
        if lista_krokow[i] == "L":
            bufor = aktualna_pozycja
            sasiedzi = komnaty[aktualna_pozycja]
            indeks_kolejnej_komnaty = sasiedzi.index(poprzednia_komnata) - 1
            aktualna_pozycja = sasiedzi[indeks_kolejnej_komnaty]
            poprzednia_komnata = bufor
        else:
            bufor = aktualna_pozycja
            sasiedzi = komnaty[aktualna_pozycja]
            indeks_kolejnej_komnaty = sasiedzi.index(poprzednia_komnata) + 1
            if indeks_kolejnej_komnaty == 3:
                indeks_kolejnej_komnaty = 0
            aktualna_pozycja = sasiedzi[indeks_kolejnej_komnaty]
            poprzednia_komnata = bufor
    return aktualna_pozycja


assert gdzie_jest_skarb("LLPPL") == "C"
