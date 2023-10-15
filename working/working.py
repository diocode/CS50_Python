import re

def main():
        print(convert(input("Hours: ").strip()))


def convert(s):
    pattern = r"((?:1[0-2]|0?[1-9])(?::[0-5][0-9])? [APap][Mm])"
    if re.match(rf"^{pattern} to {pattern}$", s):
        t1, t2 = s.split(" to ")
        t1 = single_convert(t1)
        t2 = single_convert(t2)
        return f"{t1} to {t2}"
    else:
        raise ValueError


def single_convert(s):
    parts = s.split()
    time = parts[0]
    meridian = parts[1].upper()
    if ':' in time:
        hours, minutes = map(int, time.split(':'))
    else:
        hours = int(time)
        minutes = 0
    if meridian == "PM" and hours != 12:
        hours += 12
    elif meridian == "AM" and hours == 12:
        hours = 0
    return f"{hours:02d}:{minutes:02d}"


if __name__ == "__main__":
    main()