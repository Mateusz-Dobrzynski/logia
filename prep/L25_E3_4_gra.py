# https://logia.oeiizk.waw.pl/strony/bankzadan/L25_e3_zad4.pdf

TEST_TEXT = "MXSSSXXSSSXSXSSJ"
TEST_MAZE = [
    ["M", "X", "S", "S"],
    ["S", "X", "X", "S"],
    ["S", "S", "X", "S"],
    ["X", "S", "S", "J"],
]


def game(text: str) -> str:
    maze = build_maze_from(text)
    johns_path = DFS_john_to_margaret(maze, text)
    if johns_path == "BRAK":
        return "BRAK"
    cutoff_point = len(johns_path) // 2
    margarets_path = get_margarets_path_from(johns_path)
    return f"{margarets_path}\n{johns_path[0:cutoff_point]}"


def get_margarets_path_from(johns_path: str) -> str:
    cutoff_point = len(johns_path) // 2
    second_half = johns_path[cutoff_point:]
    reversed_path = second_half[::-1]
    translated_path = reversed_path.translate(str.maketrans("DGPL", "GDLP"))
    return translated_path


def build_maze_from(text: str) -> list[list[str]]:
    maze = []
    row_length = int(len(text) ** 0.5)
    for i in range(0, row_length):
        maze.append(list(text[i * row_length : i * row_length + row_length]))
    return maze


def DFS_john_to_margaret(maze: list[list[str]], text: str):
    current_row, current_column = determine_position_of_character("J", text)
    goal_row, goal_column = determine_position_of_character("M", text)
    steps = ""
    visited_fields = set()
    stack = []
    while current_row != goal_row or current_column != goal_column:
        visited_fields.add((current_row, current_column))
        for neighbor in get_neighbors_of_current_position(
            maze, current_row, current_column
        ):
            if neighbor[0] not in visited_fields:
                stack.append(neighbor)
        try:
            next_field = stack.pop()
        except:
            return "BRAK"
        current_row = next_field[0][0]
        current_column = next_field[0][1]
        steps += next_field[1]
    return steps


def get_neighbors_of_current_position(
    maze: list[list[str]], current_row: int, current_column: int
):
    neighbors = []
    if current_row > 0:
        if maze[current_row - 1][current_column] != "X":
            neighbors.append([(current_row - 1, current_column), "G"])
    if current_row < len(maze) - 1:
        if maze[current_row + 1][current_column] != "X":
            neighbors.append([(current_row + 1, current_column), "D"])
    if current_column > 0:
        if maze[current_row][current_column - 1] != "X":
            neighbors.append([(current_row, current_column - 1), "L"])
    if current_column < len(maze) - 1:
        if maze[current_row][current_column + 1] != "X":
            neighbors.append([(current_row, current_column + 1), "P"])
    return neighbors


def determine_position_of_character(character: str, text: str) -> tuple[int, int]:
    row_length = int(len(text) ** 0.5)
    index = text.index(character)
    row = index // row_length
    column = index % row_length
    return (row, column)


assert build_maze_from(TEST_TEXT) == TEST_MAZE

assert determine_position_of_character("J", TEST_TEXT) == (3, 3)

assert get_neighbors_of_current_position(TEST_MAZE, 3, 3) == [
    [(2, 3), "G"],
    [(3, 2), "L"],
]

assert DFS_john_to_margaret(TEST_MAZE, TEST_TEXT) == "LLGLGG"

assert game("MSXJ") == "P\nG"
assert game(TEST_TEXT) == "DDP\nLLG"
assert game("MXSXSXXSSSXSXSJX") == "DDP\nLG"
assert game("MXSXSXXSSXXSXSJX") == "BRAK"
assert (
    game(
        "SSSSSXSSSSSXXXSXSXXJSSMXSXSXSXXXXXSXSXSXSSSSSXSXSXSXXXXXSXSXSXSSSXSXSXSXSXSXSXSXSXSXSXSXSSSSSXSSSXXX"
    )
    == "LLGGPPPPDDDDLLLLDDDDDPP\nGLLLDDDDDDDDDLLGGGLLDDD"
)
assert (
    game(
        "SSSXSXSXSJSXXXSXSXSXSSSXSXSXSXXXXXSXSXSXSSSSSXSXSXSXXXXXSXSXSXSSSXSXSXSXSXSXSXSXXXSXSXSXSSMSSXSSSXXX"
    )
    == "BRAK"
)
assert game("SSSSSSSXXXXSXXXXXSMXSSSXSXSXJXSSSXXX") == "DDPPG\nGLLD"
