def get_amount():
    while True:
        # Ask the user for an amount
        try:
            amount = float(input('Enter the amount: '))
            if amount < 1:
                raise ValueError()
            return amount
        # If invaild -> Print an error
        except ValueError:
            print('Invalid amount')


def get_currency(label):
    currencies = ('USD', 'EUR', 'CAD')
    # Loop
    while True:
        # Ask for the source/target currencies
        currency = input(f'{label} currency (USD/EUR/CAD): ').upper()
        # If invaild -> Print an error
        if currency not in currencies:
            print('Invalid currency')
        else:
            return currency


def convert(amount, source_currency, target_currency):
    exchange_rates = {
        'USD': {'EUR': 0.85, 'CAD': 1.25},
        'EUR': {'USD': 1.18, 'CAD': 1.47},
        'CAD': {'USD': 0.80, 'EUR': 0.68},
    }

    # Do the conversion
    if source_currency == target_currency:
        return amount

    return amount * exchange_rates[source_currency][target_currency]


def main():
    amount = get_amount()
    source_currency = get_currency('Source')
    target_currency = get_currency('Target')
    converted_amount = convert(amount, source_currency, target_currency)
    # Print the result
    print(f'{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}')


if __name__ == "__main__":
    main()
