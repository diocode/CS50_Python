import re

def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    pattern = r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    if re.match(rf"^{pattern}(\.{pattern}){{3}}$", ip):
        return True
    return False


if __name__ == "__main__":
    main()