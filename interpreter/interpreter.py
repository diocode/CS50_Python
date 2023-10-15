def main():
    x, y, z = input("Expression: ").split(" ")
    if (y == "+"):
        result = (int(x) + int(z))
    elif (y == "-"):
        result = (int(x) - int(z))
    elif (y == "*"):
        result = (int(x) * int(z))
    elif (y == "/"):
        result = (int(x) / int(z))
    print(f"{result:.1f}")

main()