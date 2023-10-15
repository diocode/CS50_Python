import sys
import emoji

def main():
    try:
        prompt = input("Input: ")
        print(emoji.emojize(prompt))
    except:
        sys.exit()

if __name__ == "__main__":
    main()