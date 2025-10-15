def decode(text: str) -> str:
    packets = text.split(" ")
    output = ""
    character_groups = [
        "0+",
        "1 ",
        "2abc",
        "3def",
        "4ghi",
        "5jkl",
        "6mno",
        "7pqrs",
        "8tuv",
        "9wxyz",
    ]
    for packet in packets:
        if packet == "*" or packet == "#":
            output += packet
            continue
        group_index = int(packet[0])
        character_position = int(packet[1]) - 1
        output += character_groups[group_index][character_position]
    return output


def test_decode():
    assert decode("92 44 64 75 63 22") == "wiosna"
    assert decode("74 64 53 12 21 01 21 21") == "rok 2022"
    assert decode("53 64 32 # 21 31 02 11 41 *") == "kod#23+14*"


test_decode()
