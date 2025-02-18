from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
import re

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']

        widgets = {
            'email':  forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo electronico',
                    'required': True,
                    'minlength': 8,
                    'maxlength': 30,
                    'pattern': '^[a-zA-Z0-9]+@utez\.edu\.mx$',
                    'title': 'Ingrese un correo válido de la UTEZ (@utez.edu.mx)'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                    'required': True,
                    'minlength': 2,  # Mínimo 2 caracteres
                    'maxlength': 50,  # Máximo 50 caracteres
                    'pattern': '^[a-zA-Z\s]+$',  # Solo letras y espacios
                    'title': 'Ingrese un nombre válido (solo letras y espacios)'
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos',
                    'required': True,
                    'minlength': 2,  # Mínimo 2 caracteres
                    'maxlength': 50,  # Máximo 50 caracteres
                    'pattern': '^[a-zA-Z\s]+$',  # Solo letras y espacios
                    'title': 'Ingrese un nombre válido (solo letras y espacios)'
                }
            ),
            'control_number': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Número de control',
                    'required': True,
                    'minlength': 8,
                    'maxlength': 10,
                    'pattern': '^[0-9]{8,10}$',  # Solo números, entre 8 y 10 dígitos
                    'title': 'Ingrese un número de control válido (8-10 dígitos numéricos)'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Edad',
                    'required': True,
                    'min': 18,  # Edad mínima
                    'max': 99,  # Edad máxima
                    'title': 'Ingrese una edad válida (entre 18 y 99 años)'
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Teléfono',
                    'required': True,
                    'minlength': 10,
                    'maxlength': 10,
                    'pattern': '^[0-9]{10}$',  # Solo 10 dígitos numéricos
                    'title': 'Ingrese un número de teléfono válido (10 dígitos numéricos)'
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Contraseña',
                    'required': True,
                    'minlength': 8,
                    'maxlength': 32,
                    'pattern': '(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,32}',  # Requisitos de complejidad
                    'title': 'La contraseña debe tener al menos 8 caracteres, incluyendo una mayúscula, un número y un carácter especial.'
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Confirme su contraseña',
                    'required': True,
                    'minlength': 8,
                    'maxlength': 32,
                    'title': 'Confirme su contraseña'
                }
            ),
        }

class CustomUserLoginForm(AuthenticationForm):
    email = forms.CharField(label="Correo electrónico", max_length=150)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and not email.endswith("@utez.edu.mx"):
            raise forms.ValidationError("El correo electrónico debe ser del dominio @utez.edu.mx.")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if password:
            # Validar que la contraseña tenga al menos 8 caracteres, al menos 1 símbolo y al menos 1 número
            if len(password) < 8:
                raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
            if not re.search(r"[!#$%&?]", password):
                raise forms.ValidationError("La contraseña debe contener al menos un símbolo (!, #, $, %, & o ?).")
            if not re.search(r"\d", password):
                raise forms.ValidationError("La contraseña debe contener al menos un número.")
        return password

    def clean_control_number(self):
        control_number = self.cleaned_data.get("control_number")
        if control_number and len(control_number) != 10:
            raise forms.ValidationError("La matrícula debe tener exactamente 10 caracteres.")
        return control_number

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data