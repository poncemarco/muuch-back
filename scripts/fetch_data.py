from items.models import Item, Category
import requests, os, json

def run():
    url = 'https://api.sheety.co/40121a2386838b1553a7e75ed35d7874/catalogoCasaMaya/catalogo'
    response = requests.get(url, verify=False)
    # with open('productos.json', 'r') as file:
    #     items = json.load(file)
    print(response.status_code)
    items = response.json()['catalogo']
    actual_categories = Category.objects.all().values_list('name', flat=True)
    categories_set  = set([category for category in actual_categories])
    categories_to_create = []
    items_in_database = Item.objects.all().values_list('external_id', flat=True)
    items_in_database = set([item for item in items_in_database])
    for item in items:
        if not 'categoria' in item or 'precio' in item:
            continue
        if item.get('category') and item.get('category') not in categories_set:
            item_category = Category(name=item.get('category'))
            categories_to_create.append(item_category)
            categories_set.add(item.get('category'))
    Category.objects.bulk_create(categories_to_create)
    items_to_create = []
    categories_id = Category.objects.all().values_list('id', 'name')
    categories_dict = {name: id for id, name in categories_id}
    for item in items:
        if 'categoria' in item and 'precio' in item:
            if item.get('id') not in items_in_database:
                item_category = categories_dict.get(item.get('categoria'))
                price = item.get('precio') if item.get('precio') else None
                item_to_create = Item(
                    name=item.get('nombre'),
                    price=price,
                    category_id=item_category,
                    unit=item.get('unidad'),
                    external_id=item.get('id')
                )
                items_to_create.append(item_to_create)
    print("Creando {} items".format(len(items_to_create)))
    Item.objects.bulk_create(items_to_create)
    print("Finalizado")