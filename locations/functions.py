import requests
from muuch_back.settings import TAU_API_KEY


def check_postal_code(postal_code: str) -> dict:
    url = f"https://api.tau.com.mx/dipomex/v1/codigo_postal?APIKEY={TAU_API_KEY}&cp={postal_code}"

    payload = {}
    headers = {
        'APIKEY': TAU_API_KEY
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    raise Exception("Error in the request")
    