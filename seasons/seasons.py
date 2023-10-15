from datetime import date
import inflect
import sys


def main():
    try:
        date = parse_date(input("Date of Birth (YYYY-MM-DD): ").strip())
        today = date.today()
        diff = today - date
        p = inflect.engine()
        print(f"{p.number_to_words(round(diff.days * 24 * 60), andword='').capitalize()} minutes")
    except ValueError:
            sys.exit("Invalid date")


def parse_date(str):
    try:
        y, m, d = str.split("-")
        return  date(int(y), int(m), int(d))
    except ValueError:
        raise ValueError


if __name__ == "__main__":
    main()