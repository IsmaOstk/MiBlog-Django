from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm


class BaseStyledForm(forms.ModelForm):
    """Formulario base del que heredan el resto. No se usa directamente."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
            raise forms.ValidationError('El título debe tener al menos 5 caracteres.')
        return titulo

    def clean_contenido(self):
        contenido = self.cleaned_data.get('contenido', '').strip()
        if len(contenido) < 20:
            raise forms.ValidationError('El contenido debe tener al menos 20 caracteres.')
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

class CustomAuthenticationForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            if not User.objects.filter(username=username).exists():
                raise forms.ValidationError(
                    'No existe ninguna cuenta con el usuario "%(username)s". '
                    '¿Querés registrarte?',
                    code='usuario_inexistente',
                    params={'username': username},
                )
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data


class PerfilForm(BaseStyledForm):
    class Meta:
        model = User
        fields = ['username', 'email']