def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    l = 0
    while l < len(s):
        if s[l].isdigit() == False and s[l].isalpha() == False:
            return False
        l += 1
    if not (2 <= len(s) <= 6):
        return False
    if not s[:2].isalpha():
        return False
    j = 2
    while j < len(s):
        if s[j].isdigit():
            if s[j] == "0":
                return False
            k = j
            while k < len(s):
                if not s[k].isdigit():
                    return False
                k += 1
            return True
        j += 1
    return True


if __name__ == "__main__":
    main()