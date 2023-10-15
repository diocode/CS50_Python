import random

def main():
    try:
        while True:
            n = input("Level: ")
            if n.isdigit() and int(n) > 0:
                break
        res = random.randrange(1, int(n) + 1)
        while True:
            guess = input("Guess: ")
            if guess.isdigit() and int(guess) > 0:
                if int(guess) < res:
                    print("Too small!")
                elif int(guess) > res:
                    print("Too large!")
                else:
                    break
        print("Just right!")
    except:
        pass

if __name__ == "__main__":
    main()