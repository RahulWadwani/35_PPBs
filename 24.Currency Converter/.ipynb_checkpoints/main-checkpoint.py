import requests

def main():
    print("\n Simple Currency Converter")
    print("Getting exchange rates...")
    try:
        res = requests.get("https://open.er-api.com/v6/latest/USD")
        rates = res.json()["rates"]
        print("Got rates successfully")
    except:
        print("Error: Couldn't connect to exchange rate API ")
        return
    print("\n popular:")
    while True:
        print("\n Enter Details: ")
        from_currency = input("From currency code (eg. USD): ").upper()
        if from_currency not in rates:
            print(f"Invalid code: {from_currency}")
            continue
        to_currency = input("To currency code (eg. EUR):").upper()
        if to_currency not in rates:
            print(f"Invalid code: {to_currency}")
            continue
        try:
            amount = float(input(f"Amount in {from_currency}:"))
        except:
            print("please enter a vlaid number")
            continue
        amount_in_usd = amount/ rates[from_currency]
        result = amount_in_usd * rates[to_currency]
        print(f"\n Results:{amount} {from_currency} = {result:.2f} {to_currency}")
        print(f"Rate: 1 {from_currency} = {rates[to_currency]/ rates[from_currency]:.4f} {to_currency}")
        if not input("\n convert again? (y/n):").lower().startswith("y"):
            print("Thanks for playing!")
            break
if __name__ == "__main__":
    main()
