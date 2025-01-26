import requests


def get_current_rate(currency_code, top_count=10):
    url = f'https://api.nbp.pl/api/exchangerates/rates/c/{currency_code}/last/{top_count}/'

    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return data['rates']


def display_data(rates):
    print("Date\t\t\tBuying Rate\t\t\tSelling Rate")
    print("============================================")
    for r in rates:
        print(f"{r['effectiveDate']}\t\t{r['bid']:.4f}\t\t\t\t{r['ask']:.4f}")


def main():
    rates = get_current_rate('eur')
    display_data(rates)


if __name__ == '__main__':
    main()