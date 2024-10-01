from items.models import Item, Category
import requests, os, json


def run():
    url = 'https://api.sheety.co/40121a2386838b1553a7e75ed35d7874/catalogoCasaMaya/catalogo'
    response = requests.get(url, verify=False)