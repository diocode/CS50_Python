def main():
    str = input("Input: ")
    print(shorten(str))


def shorten(word):
    new_word = ""
    vowels = "aeiouAEIOU"
    i = 0
    while i < len(word):
        if not word[i] in vowels:
            new_word += word[i]
        i += 1
    return new_word


if __name__ == "__main__":
    main()