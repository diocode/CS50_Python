def main():
    str = input("camelCase: ")
    print("snake_case: ", end="")
    for c in str:
        if c.isupper():
            c = "_" + c.lower()
        print(c, end="")
    print()


if __name__ == "__main__":
    main()