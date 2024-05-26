from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'profile_image', 'email', 'phone', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 2, 'cols': 30}),
        }