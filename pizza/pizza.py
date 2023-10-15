import sys
import csv
from tabulate import tabulate

def main():
    try:
        if not len(sys.argv) == 2:
            if len(sys.argv) < 2:
                sys.exit("Too few command-line arguments")
            else:
                sys.exit("Too many command-line arguments")
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        menu = []
        with open(sys.argv[1], "r") as file:
            lines = csv.reader(file)
            for Pizza, Small, Large in lines:
                menu.append({"type": Pizza, "small": Small, "large": Large})
            print(tabulate(menu, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()