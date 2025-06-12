from django.db import models

# Create your models here.
# the Card model with its fields
class Card(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    associative_imagery = models.TextField() 
    # links = реализовать связь на другие элементы bd
    # this is the image for a card, the image will be uploaded to images folder
    image = models.ImageField(null=False, blank=False, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    # this is the string representation
    # what to display after querying a card/cards
    def __str__(self):
        return f'{self.title}'
    
    # this will order the cards by date created
    class Meta:
        ordering = ['-created_at']

