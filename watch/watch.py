import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    try:
        url = []
        start = s.find("src=") + 5
        end = start
        while s[end] != "\"":
            end += 1
        url = s[start:end]
        if re.match(r"^https?://(www.)?youtube.com/embed/.+$" ,url):
            url = url[(url.find("embed/") + 6):]
            return ("https://youtu.be/" + url)
        return None
    except:
        return None


if __name__ == "__main__":
    main()
