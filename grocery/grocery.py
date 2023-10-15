def main():
    gross_list = {}
    while True:
        try:
            prompt = input().upper()
            if prompt in gross_list:
                gross_list[prompt] = gross_list[prompt] + 1
            else:
                gross_list[prompt] = 1
        except ValueError:
            pass
        except EOFError:
            for item, n in sorted(gross_list.items()):
                print(f"{n} {item}")
            break


if __name__ == "__main__":
    main()