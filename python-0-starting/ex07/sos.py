import sys


def is_valid_str(str: str) -> bool:

    """
    is_valid_str() -> bool

    Check if string only consists of alnum or spaces.
    This is by creating a new list of alnum/spaces in the str and compare
    the length of the original str and the length of the new list.
    """

    return len([x for x in str if x.isalnum() or x.isspace()]) == len(str)


def text_to_morse(str: str):

    """
    text_to_morse() -> void

    Convert the string into morse code sequence.
    The string should only consists of alphanumeric and spaces.
    """

    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        "0": "----- ",
    }

    # check if the string is valid
    assert is_valid_str(str), "found invalid characters"

    for idx, x in enumerate(str):
        code = NESTED_MORSE.get(x.upper())
        if idx == len(str) - 1:
            print(code.rstrip())
        else:
            print(code, end="")


if __name__ == "__main__":

    """main function"""

    try:
        num_of_args = len(sys.argv)
        assert num_of_args == 2, "the arguments are bad"

        text_to_morse(sys.argv[1])
    except Exception as e:
        print(f"AssertionError: {e}")
        sys.exit()
