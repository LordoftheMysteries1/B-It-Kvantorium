from django.contrib import admin
# from the models.py file import Card
from .models import Card

# registering the Card to the admin site
admin.site.register(Card)