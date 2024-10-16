def convert_currency(amount, exchange_rate):
    """Convert amount using the given exchange rate."""
    return amount * exchange_rate

def currency_converter():
    """Function to convert currencies based on user input."""
    print("Currency Converter")
    print("Available currencies:")
    print("1. USD - United States Dollar")
    print("2. EUR - Euro")
    print("3. JPY - Japanese Yen")
    print("4. INR - Indian Rupee")

    # Define exchange rates (example rates)
    exchange_rates = {
        'USD': 1.0,      # Base currency
        'EUR': 0.85,     # 1 USD = 0.85 EUR
        'JPY': 110.0,    # 1 USD = 110 JPY
        'INR': 75.0      # 1 USD = 75 INR
    }

    from_currency = input("Enter the currency you want to convert from (USD, EUR, JPY, INR): ").upper()
    to_currency = input("Enter the currency you want to convert to (USD, EUR, JPY, INR): ").upper()
    
    if from_currency in exchange_rates and to_currency in exchange_rates:
        amount = float(input(f"Enter the amount in {from_currency}: "))
        
        # Convert amount to USD first
        amount_in_usd = amount / exchange_rates[from_currency]
        
        # Convert USD to the target currency
        converted_amount = convert_currency(amount_in_usd, exchange_rates[to_currency])
        
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        print("Invalid currency input! Please enter a valid currency code.")

if __name__ == "__main__":
    currency_converter()
