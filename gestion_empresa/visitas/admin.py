from django.contrib import admin
from django.utils import timezone
from .models import Visita

# Acción personalizada para marcar salida masiva
@admin.action(description='Marcar salida para las visitas seleccionadas')
def marcar_salida_masiva(modeladmin, request, queryset):
    # Actualiza la fecha de salida a "ahora" solo si no tienen salida marcada
    queryset.filter(fecha_salida__isnull=True).update(fecha_salida=timezone.now())

class VisitaAdmin(admin.ModelAdmin):
    list_display = ('nombre_visitante', 'rut', 'fecha_ingreso', 'fecha_salida', 'estado')
    search_fields = ('rut', 'nombre_visitante') # Búsqueda por RUT
    list_filter = ('fecha_ingreso', 'fecha_salida') # Filtro por fecha
    actions = [marcar_salida_masiva] # Acción masiva

    # Método para mostrar un campo calculado en el admin
    def estado(self, obj):
        return "Finalizada" if obj.fecha_salida else "En curso"
    estado.boolean = True

admin.site.register(Visita, VisitaAdmin)