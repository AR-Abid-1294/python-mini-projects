def rateConvert(amount, source, target):
    usd_rates = {
        "USD": 1.0,
        "BDT": 122.65,
        "EUR": 0.8522,
        "GBP": 0.7435,
        "JPY": 159.17,
        "AUD": 1.4160,
        "CAD": 1.3844,
        "INR": 93.09,
        "CNY": 6.83,
        "SAR": 3.7483,
        "AED": 3.6725
    }
    usd_amount = amount / usd_rates[source]
    converted_amount = usd_amount * usd_rates[target]

    return round(converted_amount, 2)



amount = int(input("Enter the amount: "))
source = input("Source currency: ").upper()
targets = input("Target currency: ").upper().split()

for target in targets:
    result = rateConvert(amount, source, target)
    print(f"{result} {target}")



