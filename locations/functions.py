import requests


def check_postal_code(postal_code: str) -> dict:
    url = f"https://api.tau.com.mx/dipomex/v1/codigo_postal?APIKEY=7e8367808c341fd35f03170c75e420daa36e606e&cp={postal_code}"

    payload = {}
    headers = {
        'APIKEY': '7e8367808c341fd35f03170c75e420daa36e606e'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response)
    if response.status_code == 200:
        return response.json()
    raise Exception("Error in the request")