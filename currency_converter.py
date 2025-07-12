import requests

def convert_currency(from_currency, to_currency, amount):
    url = f"https://open.er-api.com/v6/latest/{from_currency.upper()}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        print("🔍 API Response:", data)

        rate = data["rates"].get(to_currency.upper())
        if rate:
            return amount * rate
        else:
            print("❌ Target currency not found.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")
        return None

def main():
    print("=== Alternate Currency Converter (ER API) ===")
    from_currency = input("Convert from (e.g. USD): ").strip()
    to_currency = input("Convert to (e.g. EUR): ").strip()
    try:
        amount = float(input("Amount to convert: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    result = convert_currency(from_currency, to_currency, amount)

    if result is not None:
        print(f"\n✅ {amount:.2f} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")

if __name__ == "__main__":
    main()
