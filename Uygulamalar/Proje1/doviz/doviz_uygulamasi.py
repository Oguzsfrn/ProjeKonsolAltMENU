import requests

def doviz_goster():
    print("Döviz Kurları Uygulaması seçildi.")
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(api_url)
    data = response.json()

    print("Döviz Kurları (USD bazında):")
    print(f"1 USD = {data['rates']['TRY']} TRY")
    print(f"1 USD = {data['rates']['EUR']} EUR")
    print(f"1 USD = {data['rates']['GBP']} GBP")
    print(f"1 USD = {data['rates']['JPY']} JPY")