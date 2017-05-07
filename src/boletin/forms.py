from django import forms

from .models import Registrado


class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["email", "nombre"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveedor = email.split("@")
        dominio, extension = proveedor.split(".")
        if not extension == "edu":
            raise forms.ValidationError
            ("Por favor utiliza un correo con la extension .edu")
        return email

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        # Validaciones a poner
        return nombre


class RegForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()


class ContactForm(forms.Form):
    nombre = forms.CharField(required=False)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveedor = email.split("@")
        dominio, extension = proveedor.split(".")
        if not extension == "edu":
            raise forms.ValidationError
            ("Por favor utiliza un correo con la extension .edu")
        return email