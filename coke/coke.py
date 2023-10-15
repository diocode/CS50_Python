def main():
    due = 50
    while due:
        print(f"Amount Due: {due}")
        credit = fcredit(input("Insert Coin: "))
        due = due - credit
        if (due <= 0):
            print(f"Change Owed: {abs(due)}")
            break


def fcredit(str):
    if (str.isdigit()):
        credit = int(str)
        if (credit == 25 or credit ==10 or credit ==5):
            return credit
    return 0

if __name__ == "__main__":
    main()