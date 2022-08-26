def reprova_comentario(modeladmin, request, queryset):
    queryset.update(aprovado=False)

def aprova_comentario(modeladmin, request, queryset):
    queryset.update(aprovado=True)

reprova_comentario.short_description = 'Reprovar comentários selecionados'
aprova_comentario.short_description = 'Aprovar comentários selecionados'