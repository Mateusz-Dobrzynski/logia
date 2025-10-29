# https://logia.oeiizk.waw.pl/strony/bankzadan/L25_e3_zad2.pdf
from math import ceil


def decrypt(input: str) -> str:
    rows = input.split("\n")
    matrix_size = int(rows[0])
    cells_count = matrix_size * matrix_size
    windows = rows[1]
    windows_count = len(windows.split(" "))
    matrix = prepare_matrix_from(matrix_size, windows)
    cipher = rows[2]
    decrypted_text = ""
    for i in range(len(cipher) // windows_count):
        cipher_portion = determine_cipher_portion(i, cipher, cells_count)
        decrypted_text += apply_matrix_to_cipher(matrix, cipher_portion)
        matrix = rotate_matrix(matrix)
    if decrypted_text.__contains__("."):
        decrypted_text = decrypted_text.split(".")[0]
    return decrypted_text


def determine_cipher_portion(rotation_index, cipher, cells_count):
    return cipher[
        rotation_index // 4 * cells_count : rotation_index // 4 * cells_count
        + cells_count
    ]


def prepare_matrix_from(table_size: int, text: str) -> list[list[int]]:
    cells = text.split(" ")
    matrix = [[0 for _ in range(table_size)] for _ in range(table_size)]
    for i in range(len(cells)):
        cell_number = int(cells[i]) - 1
        matrix[cell_number // table_size][cell_number % table_size] = 1
    return matrix


def rotate_matrix(old_matrix: list[list[int]]) -> list[list[int]]:
    matrix_size = len(old_matrix)
    new_matrix = [[-1 for _ in range(matrix_size)] for _ in range(matrix_size)]
    for i in range(matrix_size):
        current_row = old_matrix[i]
        column = matrix_size - i - 1
        for j in range(len(current_row)):
            row = j
            new_matrix[row][column] = current_row[j]
    return new_matrix


def apply_matrix_to_cipher(matrix: list[list[int]], cipher: str) -> str:
    decrypted_text = ""
    matrix_size = len(matrix)
    character_index = 0
    for i in range(matrix_size):
        for j in range(matrix_size):
            if matrix[i][j] == 1:
                character = cipher[character_index]
                decrypted_text += character
            character_index += 1
    return decrypted_text


def test_decrypt():
    assert (
        decrypt("6\n1 4 8 12 15 20 23 30 34\ncxrizboeaxwkdwaaajwwgnasikzlezoy.afa")
        == "ciekawazabawawszyfrowanie"
    )
    assert (
        decrypt("4\n1 2 11 12\nalaaaiakloamatpsmaztsajaoikovp.f")
        == "alamakotaipsaalamakotaipsa"
    )
    assert decrypt("2\n1\nabdcefhgijlk") == "abcdefghijkl"


def test_rotation():
    initial_matrix = [
        [1, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 0],
    ]

    first_turn = rotate_matrix(initial_matrix)
    second_turn = rotate_matrix(first_turn)
    third_turn = rotate_matrix(second_turn)

    assert first_turn == [
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
    ]
    assert second_turn == [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 1],
    ]
    assert third_turn == [
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
    ]


test_rotation()
test_decrypt()
