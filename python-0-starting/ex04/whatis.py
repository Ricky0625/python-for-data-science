import sys

try:
    num_of_args = len(sys.argv)

    if num_of_args < 2:
        sys.exit()
    
    assert num_of_args == 2, "more than one argument is provided"
    
    try:
        value = int(sys.argv[1])
        print("I'm Even." if value % 2 == 0 else "I'm Odd.")
    except ValueError as e:
        assert False, "argument is not an interger"

except AssertionError as ae:
    print(f"AssertionError: {ae}")