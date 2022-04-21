import requests
from pprint import pprint

CURRENCY_API_TOKEN = 'c33e4b5f488712aace7f4274'
BOT_API_TOKEN = '5302469056:AAG67EtsPh31XIk7ilJDV-yBF31rMqqfBkQ'

def get_exchange_rates(currency, token):
    """
    Returns json with currency

    
    """
    try:
        url = f'https://v6.exchangerate-api.com/v6/{token}/latest/{currency}'
        response = requests.get(url)
        data = response.json()
        return data
        
    except Exception as ex:
        print("Error!")
        
def exchange_rates_str(file, sum=1):
    """
    Returns str with currency exchange rates
    
    """
    c_USD = float(file['conversion_rates']['USD'])
    c_EUR = float(file['conversion_rates']['EUR'])
    с_PLN = float(file['conversion_rates']['PLN'])
    с_GBP = float(file['conversion_rates']['GBP'])
    с_CHF = float(file['conversion_rates']['CHF'])
    с_TRY = float(file['conversion_rates']['TRY'])
    с_CNY = float(file['conversion_rates']['CNY'])
    last_upd = file['time_last_update_utc']
    
    cur_str = f"""<b>
Долар США - {round((c_USD * sum), 3)}
Євро - {round((c_EUR * sum), 3)}
Польський Злотий - {round((с_PLN * sum), 3)} 
Фунт стерлінгів - {round((с_GBP * sum),3)}
Швейцарський фунт - {round((с_CHF * sum) ,3)}
Турецька Ліра - {round((с_TRY * sum), 3)}
Китайський Йен - {round((с_CNY * sum), 3)}</b>
<i>Оновлено - {last_upd}</i>"""
    
    print(cur_str)
    return cur_str
    
def main():
    currency = input("Enter your currency to get exchenge rates: ").upper()
    pprint(get_exchange_rates(currency, CURRENCY_API_TOKEN))
    
    
if __name__ == '__main__':
    main()
    