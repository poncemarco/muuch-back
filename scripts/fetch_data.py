from items.models import Item
import requests, os 

def run():
    url = 'https://api.sheety.co/40121a2386838b1553a7e75ed35d7874/productos/catalogo'
    response = requests.get(url)
    items = response.json()['catalogo']
    print(items)
    for item in items:
        if not Item.objects.filter(name=item['producto'].strip()).exists():
            Item.objects.create(name=item['producto'], price=float(item['categori']), unit=item['unidad'], category=item['categoria'])
            print(f"Producto {item['producto']} creado") 
        else:
            print(f"Producto {item['producto']} ya existe")
    print("Finalizado")