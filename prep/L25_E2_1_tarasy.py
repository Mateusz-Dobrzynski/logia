# https://logia.oeiizk.waw.pl/strony/bankzadan/L25_e2_zad1.pdf

from turtle import *
from math import sqrt

SINGLE_SIDE_WIDTH = 300


def initial_position(left_side=True):
    penup()
    if left_side:
        modifier = -1
    else:
        modifier = 1
    goto(300.0 * modifier, -150)


def tarasy(number: int):
    numbers = list(str(number))
    left_side_size = count_numbers(numbers, odd=False)
    right_side_sice = count_numbers(numbers, odd=True)
    draw_terraces(left_side_size, right_side_sice)
    done()


def draw_terraces(left_side_size: int, right_side_size: int):
    initial_position(left_side=True)
    left(90)
    draw_side(left_side_size, left_side=True)
    initial_position(left_side=False)
    draw_side(right_side_size, left_side=False)
    initial_position(left_side=True)
    right(90)
    pendown()
    forward(600)


def draw_side(terraces_count, left_side=True):
    terrace_size = SINGLE_SIDE_WIDTH / (terraces_count + 1)
    pendown()
    for _ in range(terraces_count):
        draw_terrace(terrace_size, left_side)
    turn_right_on_left(45, left_side)
    forward(terrace_size * sqrt(2))
    turn_right_on_left(-45, left_side)


def turn_right_on_left(degree: float, left_side=True):
    if left_side:
        right(degree)
    else:
        left(degree)


def draw_terrace(size: int, left_side=True):
    forward(size)
    turn_right_on_left(90, left_side)
    forward(size)
    turn_right_on_left(-90, left_side)


def count_numbers(numbers: list[str], odd: bool) -> int:
    counter = 0
    for number in numbers:
        if odd and int(number) % 2 == 1:
            counter += 1
        elif not odd and int(number) % 2 == 0:
            counter += 1
    return counter


tarasy(2648)
