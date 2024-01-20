from django.db import models

class Image(models.Model):
    item = models.ForeignKey('items.Item', on_delete=models.CASCADE, related_name='images')
    image_path = models.CharField(max_length=400)

    def __str__(self):
        return self.item.name + " - " + str(self.id)
