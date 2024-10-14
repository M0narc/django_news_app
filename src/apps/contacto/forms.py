from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Nombre')
    email = forms.EmailField(required=True, label='Correo Electrónico')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Mensaje')
