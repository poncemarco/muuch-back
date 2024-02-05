from items.models import Item

def run():
    items = Item.objects.all()
    for item in items:
        try:
            if not item.images.exists():
                name = item.name.replace(" ", "+").rstrip('.') 
                item.images.create(image_path=f"images/products_images/{name} Background Removed.png")
                print(f"Imagen para {item.name} creada")
            else:
                print(f"Imagen para {item.name} ya existe")
        except:
            print(f"Imagen para {item.name} no encontrada")
            
    print("Finalizado")