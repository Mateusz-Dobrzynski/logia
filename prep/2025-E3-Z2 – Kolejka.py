MAX_QUEUE_LENGTH = 10000


def queue_finder(input: str) -> str:
    rows = input.split("\n")
    searched_students_count = rows[0]
    queue = rows[1].split(" ")
    shortest_subqueue_index = -1
    shortest_subqueue_length = MAX_QUEUE_LENGTH + 1
    for i in range(len(queue)):
        current_student = queue[i]
        students_left = int(searched_students_count) - 1
        j = i + 1
        subqueue_length = 1
        while students_left > 0:
            try:
                next_student = queue[j]
                subqueue_length += 1
            except:
                break
            if next_student == current_student:
                students_left -= 1
                if students_left == 0 and subqueue_length < shortest_subqueue_length:
                    shortest_subqueue_length = subqueue_length
                    shortest_subqueue_index = i + 1
            j += 1
    return f"{shortest_subqueue_index} {shortest_subqueue_length}"


def test_queue():
    assert queue_finder("3\n2 3 1 2 1 3 1 1 2") == "5 4"
    assert queue_finder("3\n1 2 3 2 3 3 4 2 1 4 3 2 1 4 2 1 2") == "3 4"
    assert queue_finder("5\n2 3 1 3 2 1 3 2 2 1 3 1 3 1 2 3 3 3 1 1 2") == "11 8"


test_queue()
