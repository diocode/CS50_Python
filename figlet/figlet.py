from pyfiglet import Figlet
from pyfiglet import FigletFont
import sys
import random

def main():
    try:
        if not check_args():
            sys.exit("Invalid usage")
        prompt = input("Input: ")
        if len(sys.argv) == 3:
            cstr = Figlet(font=sys.argv[2])
        else:
            cstr = Figlet(font=random.choice(FigletFont.getFonts()))
        print (f"Output:\n{cstr.renderText(prompt)}")
    except:
        sys.exit("Invalid usage")

def check_args():
    if len(sys.argv) != 3 and len(sys.argv) != 1:
        return False
    if len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            return False
        for font in FigletFont.getFonts():
            if font == sys.argv[2]:
                return True
    return False


if __name__ == "__main__":
    main()