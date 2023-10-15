def main():
    while True:
        try:
            fuel = convert(input("Fraction: "))
            print(f"{gauge(fuel)}",)
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = fraction.split("/")
    if int(y) <= 0:
        raise ZeroDivisionError
    if not x.isdigit() or not y.isdigit() or int(x) > int(y):
        raise ValueError
    else:
        return round(int(x) / int(y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()