from items.models import Item, Category
import requests, os, json

def run():
    # url = 'https://api.sheety.co/40121a2386838b1553a7e75ed35d7874/productos/catalogo'
    # response = requests.get(url)
    with open('productos.json', 'r') as file:
        items = json.load(file)
    
    # items = response.json()['catalogo']
    # return print(items["catalogo"])
    for item in items["catalogo"]:
        if not Item.objects.filter(name=item['item'].strip()).exists() and hasattr(item, 'price'):
            category, _ = Category.objects.get_or_create(name=item['categoria'])
            Item.objects.create(name=item['item'], 
                                price=item["precio"], 
                                unit=item['unidad'], 
                                category=category
                                )
            print(f"Producto {item['item']} creado") 
        else:
            print(f"Producto {item['item']} ya existe")
    print("Finalizado")