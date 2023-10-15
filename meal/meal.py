def main():
    str = input("What time is it? ")
    time = convert(str)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    hour, min = time.split(":")
    if min.endswith("m."):
        new_min, flg = min.strip().split(" ")
        if (flg == "p.m."):
            hour = float(hour) + 12
        else:
             hour = float(hour)
        min = float(new_min) / 60
    else:
        hour = float(hour)
        min = float(min) / 60
    return hour + min

if __name__ == "__main__":
    main()