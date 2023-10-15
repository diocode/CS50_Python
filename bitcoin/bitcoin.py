import requests
import sys

def main():
    try:
        if len(sys.argv) != 2:
            sys.exit(1)
        n = float(sys.argv[1])
        price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        price = float(price["bpi"]["USD"]["rate_float"])
        print(f"${n * price:,.4f}")
    except requests.RequestException:
        pass
    except ValueError:
        sys.exit("Command-line argument is not a number")

if __name__ == "__main__":
    main()

