from forex_python.converter import CurrencyRates

currencies = {
    "1": "USD",
    "2": "EUR",
    "3": "GBP",
    "4": "INR",
    "5": "JPY",
    "6": "CAD",
    "7": "AUD",
    "8": "CHF",
    "9": "CNY",
    "10": "SEK",
    "11": "NOK"
}

def Currency_options():
    print("Currency Exchanger")
    print("1. USD (United States Dollar)")
    print("2. EUR (Euro)")
    print("3. GBP (British Pound)")
    print("4. INR (Indian Rupee)")
    print("5. JPY (Japanese Yen)")
    print("6. CAD (Canadian Dollar)")
    print("7. AUD (Australian Dollar)")
    print("8. CHF (Swiss Franc)")
    print("9. CNY (Chinese Yuan)")
    print("10. SEK (Swedish Krona)")
    print("11. NOK (Norwegian Krone)")

def user_choice():
    base_currency = ""
    target_currency = ""

    choice1 = input("Enter the Base currency (1/2/3/4/5/6/7/8/9/10/11): ")
    if choice1 in currencies:
        base_currency = currencies[choice1]

    choice2 = input("Enter the Target currency (1/2/3/4/5/6/7/8/9/10/11): ")
    if choice2 in currencies:
        target_currency = currencies[choice2]

    return base_currency, target_currency

def currency_conversion(base_currency, target_currency):
    c = CurrencyRates()
    amount = float(input(f"Enter the amount to be converted from {base_currency} to {target_currency}: "))
    conversion = c.convert(base_currency, target_currency, amount)
    print(f"{amount} {base_currency} = {conversion} {target_currency}")

def main():
    Currency_options()
    base_currency, target_currency = user_choice()
    currency_conversion(base_currency, target_currency)

main()
