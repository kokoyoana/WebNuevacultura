from django import forms


class Formulario(forms.Form):
    nombre = forms.CharField(label='Nombre',max_length=100)
    mensaje = forms.CharField(label='Mensaje',widget=forms.Textarea,max_length=1000)
    email = forms.EmailField(label='correo electronico')