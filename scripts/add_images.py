from items.models import Item
import os
import urllib.parse
from files.models import Image


def run():
    items = Item.objects.filter(images__isnull=False)
    items_no_images = Item.objects.filter(images__isnull=True)
    images_database = [urllib.parse.unquote_plus(item.images.all().first().image_path.url.split("/")[4]) for item in items]
    
    errors = []
    create = []
    files = os.listdir("media/images/products_images")
    files = [file.replace("+", " ").replace("-", "/").replace("_", ".") for file in files]
    for file in files:
        if file not in images_database:
            item = items_no_images.filter(name=file.replace(" Background Removed.png", ""))
            if item.exists() and item.first().main_image:
                file_name = file.replace(" ", "+").replace("+Background+Removed.png", "").replace("/", "-").replace(".", "_") + " Background Removed.png"
                image = Image.objects.create(
                    item=item.first(),
                    image_path=f"images/products_images/{file_name}")
                create.append(f"Image {file} created")
                continue
            else:
                item = items_no_images.filter(name=file.replace(" Background Removed.png", "") + ".")
                if item.exists():
                    file_name = file.replace(" Background Removed.png", "").replace(" ", "+").replace("/", "-").replace(".png", "").replace(".", "_") + " Background Removed.png"
                    print(file_name)
                    try:
                        Image.objects.create(item=item.first(), image_path=f"images/products_images/{file_name}")
                        create.append(f"Image {file} created")
                        continue
                    except FileNotFoundError:
                        errors.append(f"Item {file_name} not found")  
                        
    print(f"errors {errors}, create {create}")