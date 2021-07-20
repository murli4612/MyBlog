from django.db import models
from django import forms

# Create your models here.
class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     namea= models.CharField(max_length=255)
     phonea= models.CharField(max_length=13)
     emaila= models.CharField(max_length=100)
     contenta= models.TextField()
     timeStampa=models.DateTimeField(auto_now_add=True, blank=True)
     
     def __str__(self):
          return "Message from " + self.namea + ' - ' + self.emaila    


# class GeeksForm(forms.Form):
#      ttitle = forms.CharField()
#      description = forms.CharField()
#      available = forms.BooleanField()
#      email = forms.EmailField()
     
class GeeksModel(models.Model):
        # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add = True)
    img = models.ImageField(upload_to = "imgges/" , default="")
   
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.title     