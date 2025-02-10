import requests
import os
from dotenv import load_dotenv

load_dotenv()

base_url = "https://mt-client-api-v1.london.agiliumtrade.ai"
headers = {
    'auth-token': os.environ.get('METATAPI_API_KEY')
}
ACCOUNT_ID = os.environ.get('METAAPI_ACCOUNT_ID')

def get_account_info():
    url = base_url + f"/users/current/accounts/{ACCOUNT_ID}/account-information"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else :
        print(f"Error: {response.status_code}")
        return None

def get_open_trades():
    url = base_url + f"/users/current/accounts/{ACCOUNT_ID}/positions"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else :
        print(f"Error: {response.status_code}")
        return None
