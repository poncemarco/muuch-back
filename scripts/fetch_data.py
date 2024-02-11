from items.models import Item, Category
import requests, os, json

def run():
    url = 'https://api.sheety.co/40121a2386838b1553a7e75ed35d7874/catalogoCasaMaya/catalogo'
    response = requests.get(url, verify=False)
    # with open('productos.json', 'r') as file:
    #     items = json.load(file)
    
    items = response.json()['catalogo']
    print(items)
    # return print(items["catalogo"])
    for item in items:
        if 'categoria' in item and 'precio' in item:
            category, created = Category.objects.get_or_create(name=item['categoria'])
            item['categoria'] = category
            item_, _ = Item.objects.get_or_create(name=item['productos'], category=item['categoria'], price=item['precio'])
            if _:
                print(f"Item {item['productos']} created")
    print("Finalizado")