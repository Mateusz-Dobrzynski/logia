from math import *


def numbers_search(number: int) -> str:
    found_numbers = []
    candidate = number + 1
    while len(found_numbers) < 5:
        average = get_average_of_divisors_of_composite_number(candidate)
        square_root = sqrt(candidate)
        if average == -1:
            candidate += 1
            continue
        if average <= square_root:
            found_numbers.append(candidate)
        candidate += 1
    # Return a str containing list elements separated with whitespace
    return " ".join(map(str, found_numbers))


def get_average_of_divisors_of_composite_number(number: int) -> float:
    divisors = [1]
    # Check if the number is prime and return -1, if it does
    for i in range(2, ceil(number / 2) + 1):
        if i > floor(sqrt(number)) and len(divisors) == 1:
            return -1
        if number % i == 0:
            divisors.append(i)
    average = sum(divisors) / len(divisors)
    return average


def test_divisors_average_calculation():
    assert get_average_of_divisors_of_composite_number(6) == 2
    assert get_average_of_divisors_of_composite_number(41) == -1


def test_divisor_search():
    assert numbers_search(40) == "45 49 51 55 65"
    assert numbers_search(302) == "319 323 341 361 377"


test_divisors_average_calculation()
test_divisor_search()
