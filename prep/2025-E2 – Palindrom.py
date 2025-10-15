def palindrome(text: str) -> str:
    palindrome_start = ""
    palindrome_end = ""
    middle_letter = ""
    letters = list(text)
    letters.sort()
    i = 1
    while i < len(letters):
        current_letter = letters[i]
        previous_letter = letters[i - 1]
        if current_letter == previous_letter:
            palindrome_start = f"{palindrome_start}{current_letter}"
            palindrome_end = f"{current_letter}{palindrome_end}"
            i += 1
        elif middle_letter == "":
            middle_letter = previous_letter
        i += 1
    return f"{palindrome_start}{middle_letter}{palindrome_end}"


def test_palindrome():
    assert palindrome("abrakadabrahokuspokus") == "aabkorsuausrokbaa"
    assert palindrome("zlwurgbsfyexkqndcoihtmpvj") == "b"
    assert palindrome("aabba") == "ababa"


test_palindrome()
