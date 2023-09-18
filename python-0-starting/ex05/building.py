import sys


"""
list comprehension offers a shorter syntax when you want to
create a new list based on the values of an existing list.

This is the same as...

    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = []

    for x in fruits:
      if "a" in x:
        newlist.append(x)

...this:

    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [x for x in fruits if "a" in x]

"""


def count_upper(input: str) -> int:

    """count uppercase letters"""

    return len([x for x in input if x.isupper()])


def count_lower(input: str) -> int:

    """count lowercase letters"""

    return len([x for x in input if x.islower()])


def count_punctuation(input: str) -> int:

    """count punctuation marks"""

    # triple single quotes are used to create multiline string literals
    # can inlude line breaks without the need for escaping characters
    marks = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
    return len([x for x in input if x in marks])


def count_space(input: str) -> int:

    """count spaces, including newline/carriage return"""

    return len([x for x in input if x.isspace()])


def count_digit(input: str) -> int:

    """count digits"""

    return len([x for x in input if x.isdigit()])


def count_and_print(input: str):

    """call all the counter function and print the value out"""

    print(f"The text contains {len(input)} characters:")
    print(f"{count_upper(input)} upper letters")
    print(f"{count_lower(input)} lower letters")
    print(f"{count_punctuation(input)} punctuation marks")
    print(f"{count_space(input)} spaces")
    print(f"{count_digit(input)} digits")


def read_input() -> str:

    """
    read input from stdin. will return the str when encounter EOF (CTRL+D)
    """

    str = ""
    try:
        print("What is the text to count?")
        str = sys.stdin.readline()
    except EOFError:
        pass
    return str


def get_input() -> str:

    """
    Try to get the string from argv first.
    Number of argument should be less than or equal to 2,
    meaning it has either one arg or none.
    If it has 1 arg, return argv[1]
    Else read input from stdin
    """

    try:
        num_of_args = len(sys.argv)
        assert num_of_args <= 2, "more than one argument is provided"
        if num_of_args == 2:
            return (sys.argv[1])
        else:
            input = read_input()
            return input if input is not None else ""
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit()


def main():

    """
    1. get input
    2. count and print
    """

    input = get_input()
    count_and_print(input)


if __name__ == "__main__":
    main()
