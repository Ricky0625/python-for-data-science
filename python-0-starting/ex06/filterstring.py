import sys
from ft_filter import ft_filter


def is_valid_str(str: str) -> bool:

    """
    is_valid_str() -> bool

    Check if string only consists of alnum or spaces.
    This is by creating a new list of alnum/spaces in the str and compare
    the length of the original str and the length of the new list.
    """

    return len([x for x in str if x.isalnum() or x.isspace()]) == len(str)


def filterstring():

    """
    filterstring() -> void

    Check if number of arguments is 3 & the str consists only alnum or spaces.
    Split the words by whitespaces, and create a lambda function based on
    num_of_args. The lambda function is then passed into ft_filter. ft_filter
    will create a new list which is a list of filtered items.
    """

    try:
        # check number of argument
        num_of_args = len(sys.argv)
        assert num_of_args == 3

        # validate string if it only consists of alnum or spaces
        arg = sys.argv[1]
        assert is_valid_str(arg)

        # split by spaces
        value_strs = arg.split()
        value_len = int(sys.argv[2])
        new_strs = ft_filter(lambda str: len(str) > value_len, value_strs)
        return new_strs
    except Exception:
        print("AssertionError: the arguments are bad")
        sys.exit()


if __name__ == "__main__":
    strs = filterstring()
    print(strs)
