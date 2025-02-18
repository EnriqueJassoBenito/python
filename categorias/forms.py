# Que define los formularios de los modelos en esta app

from django import forms
from .models import Categoria

# Se debe crear una clase para cada modelo
class categoriaForm(forms.ModelForm):
    # Meta es la clase que define la meta-informacion del formulario
    class Meta:
        model = Categoria
        fields = ['nombre', 'imagen']
        
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'forms-input',
                    'placeholder': 'Nombre del producto'
                }
            ),
            'imagen': forms.URLInput(
                attrs = {
                    'class': 'forms-input',
                    'placeholder': 'Imagen de la categoria'
                }
            )
        }
        
        # Personalizar las etiquetas
        labels = {
            'nombre': 'Nombre del producto',
            'imagen': 'URL de la imagen'
        }
        
        # Mensajes de error
        error_messages = {
            'nombre': {
                'required': 'El nombre es obligatorio'
            },
            'imagen': {
                'required': 'El precio no puede estar vacio',
                'invalid': 'Ingresa un numero valido'
            }
        }