import requests
import sys

def main():
    if len(sys.argv) < 1:
        print('Missing command-line argument')
        sys.exit()

    try:
        bitcoins = float(sys.argv[1]) #Este es el input del usuario <----------
    except ValueError:
        print('Missing command-line argument')
        sys.exit(1)

    while True:
        try:
            r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            total = bitcoins * (r.json()['bpi']['USD']['rate_float'])
            print(f'${total:,.4f}')
            break
        except requests.RequestException:
            break



if __name__ == "__main__":
    main()
