import random
import sys


def main():
    n = get_level()
    score = 0
    for _ in range(10):
        tries = 0
        x = generate_integer(n)
        y = generate_integer(n)
        while True:
            prompt = int(input(f"{x} + {y} = "))
            if prompt == x + y:
                score += 1
                break
            tries += 1
            if tries == 3:
                print(f"{x} + {y} = {x + y}")
                break
            print("EEE")
    print(f"Score: {score}")


def get_level():
    try:
        while True:
            n = input("Level: ")
            if n.isdigit() and 1 <= int(n) <= 3:
                return int(n)
    except:
        sys.exit()


def generate_integer(level):
     min = 10 ** (level - 1)
     max = (10 ** level) - 1
     if level == 1:
        min -= 1
     return random.randint(min, max)


if __name__ == "__main__":
    main()