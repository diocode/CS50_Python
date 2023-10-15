import sys
import csv

def main():
    try:
        if not len(sys.argv) == 3:
            if len(sys.argv) < 3:
                sys.exit("Too few command-line arguments")
            else:
                sys.exit("Too many command-line arguments")
        new_csv = []
        with open(sys.argv[1], "r") as file:
            lines = csv.reader(file)
            next(lines)
            for name, house in lines:
                last, first = name.split(",")
                new_csv.append({"first": first.lstrip(), "last": last, "house": house})
        with open(sys.argv[2], "w") as new:
            writer = csv.writer(new)
            new.write("first,last,house\n")
            for line in new_csv:
                writer.writerow(line.values())
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()