from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/nuevo/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/editar/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/eliminar/', views.PostDeleteView.as_view(), name='post_delete'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.PerfilView.as_view(), name='perfil'),
path('perfil/editar/', views.PerfilUpdateView.as_view(), name='perfil_editar'),
]