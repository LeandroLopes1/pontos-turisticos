from django.contrib import admin
from .models import Comentario
from .actions import reprova_comentario, aprova_comentario

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'comentario', 'aprovado']
    actions = [reprova_comentario, aprova_comentario]

admin.site.register(Comentario, ComentarioAdmin)
