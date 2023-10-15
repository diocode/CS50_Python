import sys
from PIL import Image
from PIL import ImageOps

def main():
    try:
        if not len(sys.argv) == 3:
            if len(sys.argv) < 3:
                sys.exit("Too few command-line arguments")
            else:
                sys.exit("Too many command-line arguments")
        if check_ext(sys.argv[1]) or check_ext(sys.argv[2]):
            sys.exit("Invalid input")
        if not iscompatible(sys.argv[1], sys.argv[2]):
            sys.exit("Input and output have different extensions")
        input_img = Image.open(sys.argv[1])
        overlay_img = Image.open("shirt.png")
        input_img = ImageOps.fit(input_img, overlay_img.size, method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        new_img = Image.new("RGB", input_img.size)
        new_img.paste(input_img, (0, 0))
        new_img.paste(overlay_img, (0, 0), overlay_img)
        new_img.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("File does not exist")


def check_ext(str):
     if str.endswith(".jpg") or str.endswith(".jpeg") or str.endswith(".png"):
         return False
     return True


def iscompatible(str1, str2):
    if str1.endswith(".jpeg"):
        n = 5
    else:
        n = 4
    return str1[-n:] == str2[-n:]


if __name__ == "__main__":
    main()