from django.contrib import admin
# from django import forms
from .models import Contact
from .models import GeeksModel

# Register your models here.
admin.site.register(Contact)
admin.site.register(GeeksModel)

