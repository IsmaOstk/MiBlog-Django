from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post



class BaseStyledForm(forms.ModelForm):
    """
    Formulario base del que heredan el resto de los formularios del proyecto.
    No se usa directamente: define comportamiento y estilo comunes.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Recorre todos los campos del formulario (los que definan las
        # subclases) y les agrega la clase CSS 'form-control', además de
        # un placeholder automático con el nombre del campo.
        for nombre_campo, campo in self.fields.items():
            campo.widget.attrs.update({
                'class': 'form-control',
                'placeholder': campo.label or nombre_campo.capitalize(),
            })

class PostForm(BaseStyledForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido']

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo', '').strip()
        if len(titulo) < 5:
            raise forms.ValidationError(
                'El título debe tener al menos 5 caracteres.'
            )
        return titulo

    def clean_contenido(self):
        contenido = self.cleaned_data.get('contenido', '').strip()
        if len(contenido) < 20:
            raise forms.ValidationError(
                'El contenido debe tener al menos 20 caracteres.'
            )
        return contenido
    
    class RegistroForm(BaseStyledForm, UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Ya existe una cuenta con ese email.')
        return email