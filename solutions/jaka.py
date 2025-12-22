def suma_cyfr(liczba: int) -> int:
    liczba = list(str(liczba))
    suma = 0
    for i in range(len(liczba)):
        suma += int(liczba[i])
    return suma


def jaka(minimum, maximum, ktora_z_kolei):
    k = 0
    for i in range(1, 100001):
        suma = suma_cyfr(i)
        if suma > minimum and suma < maximum:
            k += 1
        if k == ktora_z_kolei:
            return i
    return -1


assert suma_cyfr(10) == 1
assert suma_cyfr(15100900) == 16

assert jaka(1, 10, 4) == 5
assert jaka(1, 3, 100) == -1
