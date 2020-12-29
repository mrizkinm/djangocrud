from django import forms
from .models import Contact
from .models import Cars
from .models import Rent

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = "__all__"

class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = "__all__"