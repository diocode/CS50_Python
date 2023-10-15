import re

def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"(?i)(^|[^a-z])um([^a-z]|$)"
    if matches := re.findall(pattern, s):
        return len(matches)
    else:
        return 0


if __name__ == "__main__":
    main()
