import inflect

def main():
    lst = []
    try:
        while True:
            lst.append(input("Name: "))
    except EOFError:
        print(f"Adieu, adieu, to {inflect.engine().join(lst)}")

if __name__ == "__main__":
    main()