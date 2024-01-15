from django.contrib import admin
from app.models import *

# ! Crear base para que el created_by y updated_by se rellenen automaticamente
class BaseModelAdmin(admin.ModelAdmin):
    exclude = ('created_by', 'updated_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)


# ! usar la base para habilidades
class HabilidadAdmin(BaseModelAdmin):
    pass

# ! usar la base para estudios
class EstudioAdmin(BaseModelAdmin):
    pass

# ! usar la base para categorias
class CategoriaAdmin(BaseModelAdmin):
    pass

# ! usar la base para experiencias
class ExperienciaAdmin(BaseModelAdmin):
    pass

# ! usar la base para seguidores
class SeguidorAdmin(BaseModelAdmin):
    pass

# ! usar la base para seguidos
class SeguidosAdmin(BaseModelAdmin):
    pass

# ! usar la base para notificaciones
class NotificacionAdmin(BaseModelAdmin):
    pass

# Register your models here.
admin.site.register(Habilidad, HabilidadAdmin)
admin.site.register(Estudio, EstudioAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Experiencia, ExperienciaAdmin)
admin.site.register(Seguidor, SeguidorAdmin)
admin.site.register(Seguidos, SeguidosAdmin)
admin.site.register(Notificacion, NotificacionAdmin)
