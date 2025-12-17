def prelekcje(czasy_rozpoczecia: str) -> int:
    # zaminiemay casy na min
    # liczymy końce preleckcji
    # sotrujemy po czasie zakonczenia
    # zliczamy ile możemy odwiedzić
    czasy_prelekcji = []
    czasy_rozpoczecia = czasy_rozpoczecia.split(" ")
    for i in range(len(czasy_rozpoczecia)):
        minuty_rozpoczecia = godz_na_min(czasy_rozpoczecia[i])
        czasy_prelekcji.append(
            [minuty_rozpoczecia, koniec_prelekcji(minuty_rozpoczecia)]
        )
    czasy_prelekcji.sort(key=lambda prelekcja: prelekcja[1])
    return ile_odwiedzic(czasy_prelekcji)


def godz_na_min(czas_rozpoczecia_prelekcji: str) -> int:
    godz, minuty = czas_rozpoczecia_prelekcji.split(":")
    return int(godz) * 60 + int(minuty)


assert godz_na_min("10:05") == 605
assert godz_na_min("10:45") == 645
assert godz_na_min("11:00") == 660


def koniec_prelekcji(godz_rozpoczecia_min: int) -> int:
    czas_prelekcji = godz_rozpoczecia_min // 60
    if czas_prelekcji % 2 == 0:
        koniec = godz_rozpoczecia_min + 15
    else:
        koniec = godz_rozpoczecia_min + 20
    return koniec


assert koniec_prelekcji(645) == 660
assert koniec_prelekcji(605) == 620
assert koniec_prelekcji(660) == 680


def ile_odwiedzic(posortowane_czasy_prelekcji: list[list[int]]) -> int:
    aktualna_godz = posortowane_czasy_prelekcji[0][1]
    ilosc_odwiedzonych = 1
    for i in range(1, len(posortowane_czasy_prelekcji)):
        if aktualna_godz <= posortowane_czasy_prelekcji[i][0]:
            ilosc_odwiedzonych += 1
            aktualna_godz = posortowane_czasy_prelekcji[i][1]
    return ilosc_odwiedzonych


assert prelekcje("11:00 10:45") == 2
assert prelekcje("10:59 11:00 11:59 12:00 12:59 13:00 13:59 14:00") == 4
