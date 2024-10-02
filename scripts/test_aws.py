import boto3

s3 = boto3.client('s3')

# Prueba de subida
def run():
    try:
        s3.upload_file('media/images/products_images/ACEITE+AJONJOLI+TOSTADO+INES+250+ML Background Removed.png', 'muuch-bucket', 'images/products_images/test_file.png')
        print("Archivo subido correctamente.")
    except Exception as e:
        print("Error al subir el archivo:", e)
