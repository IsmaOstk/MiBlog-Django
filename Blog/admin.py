# blog/admin.py
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion')
    list_filter = ('autor', 'fecha_creacion')
    search_fields = ('titulo', 'contenido')
    ordering = ('-fecha_creacion',)