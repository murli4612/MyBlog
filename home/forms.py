# import form class from django
from django import forms


# import GeeksModel from models.py
from .models import GeeksModel

# create a ModelForm
class GeeksForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = GeeksModel
		fields = "__all__"
# creating a form
class InputForm(forms.Form):
 
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(
                     help_text = "Enter 6 digit roll number"
                     )
    password = forms.CharField(widget = forms.PasswordInput())

from django import forms


class SubscribeForm(forms.Form):
    email = forms.EmailField()