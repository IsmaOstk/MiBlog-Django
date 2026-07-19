from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q



class Post(models.Model):
    """Representa una entrada de blog."""

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_creacion']  # más nuevos primero

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        """URL a la que se redirige tras crear/editar un post."""
        return reverse('post_detail', kwargs={'pk': self.pk})
    
def get_queryset(self):
    queryset = super().get_queryset()
    autor = self.request.GET.get('autor')
    q = self.request.GET.get('q')
    if autor:
        queryset = queryset.filter(autor__username__icontains=autor)
    if q:
        queryset = queryset.filter(
            Q(titulo__icontains=q) | Q(contenido__icontains=q)
        )
    return queryset