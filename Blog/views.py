from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post
from .forms import PostForm, RegistroForm
from django.contrib.auth.views import LoginView
from .forms import PostForm, RegistroForm, CustomAuthenticationForm, PerfilForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView


# ---------- Registro ----------
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('post_list')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})


# ---------- READ: listado con búsqueda por autor ----------
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        autor = self.request.GET.get('autor')
        if autor:
            # búsqueda case-insensitive por nombre de usuario del autor
            queryset = queryset.filter(autor__username__icontains=autor)
        return queryset


# ---------- READ: detalle de un post ----------
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# ---------- CREATE ----------
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    login_url = 'login'

    def form_valid(self, form):
        # asigna automáticamente el autor = usuario logueado
        form.instance.autor = self.request.user
        return super().form_valid(form)


# ---------- UPDATE ----------
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    login_url = 'login'

    def test_func(self):
        # solo el autor puede editar su propio post
        post = self.get_object()
        return self.request.user == post.autor


# ---------- DELETE ----------
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    login_url = 'login'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor
    
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm


class PerfilView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'registration/perfil.html'
    context_object_name = 'usuario'
    login_url = 'login'

    def get_object(self):
        return self.request.user


class PerfilUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = PerfilForm
    template_name = 'registration/perfil_form.html'
    success_url = reverse_lazy('perfil')
    login_url = 'login'

    def get_object(self):
        return self.request.user
    
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('perfil')  # en vez de password_change_done