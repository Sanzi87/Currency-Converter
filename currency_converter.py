# Loop
while True:
    # Ask the user for an amoint
    try:
        amount = float(input('Enter the amount: '))
        if amount < 1:
            raise ValueError()
        break
    # If invaild -> Print an error
    except ValueError:
        print('Invalid amount')

currencies = ('USD', 'EUR', 'CAD')
# Loop
while True:
    # Ask for the source currency
    source_currency = input('Source currency (USD/EUR/CAD): ').upper()
    # If invaild -> Print an error
    if source_currency not in currencies:
        print('Invalid currency')
    else:
        break
# Loop
while True:
    # Ask for the target currency
    target_currency = input('Target currency (USD/EUR/CAD): ').upper()
    # If invaild -> Print an error
    if target_currency not in currencies:
        print('Invalid currency')
    else:
        break

exchange_rates = {
    'USD': {'EUR': 0.85, 'CAD': 1.25},
    'EUR': {'USD': 1.18, 'CAD': 1.47},
    'CAD': {'USD': 0.80, 'EUR': 0.68},
}

# Do the conversion
if source_currency == target_currency:
    converted_amount = amount
else:
    converted_amount = amount * \
        exchange_rates[source_currency][target_currency]
# Print the result
print(f'{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}')
