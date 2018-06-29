from django.forms import ModelForm, CharField
from posts.models import Contacts

class ContactForm(ModelForm):
 
 class Meta:
    model = Contacts
    fields = ['first_name', 'last_name','image', 'phone_number', 'email', 'favourite']