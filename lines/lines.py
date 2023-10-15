import sys

def main():
    try:
        if not len(sys.argv) == 2:
            if len(sys.argv) < 2:
                sys.exit("Too few command-line arguments")
            else:
                sys.exit("Too many command-line arguments")
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
        count = 0
        for line in lines:
            if not line.lstrip().startswith("#") and not line.isspace():
                count += 1
        print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()