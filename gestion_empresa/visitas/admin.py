from django.contrib import admin
from django.utils import timezone
from django.utils.safestring import mark_safe # <--- ESTO ES LO NUEVO (Más seguro)
from .models import Visita

# Acción para marcar salida masiva
@admin.action(description='Marcar salida para seleccionados')
def marcar_salida_masiva(modeladmin, request, queryset):
    queryset.filter(fecha_salida__isnull=True).update(fecha_salida=timezone.now())

class VisitaAdmin(admin.ModelAdmin):
    # Asegúrate que 'estado_visual' esté aquí tal cual se escribe abajo
    list_display = ('nombre_visitante', 'rut', 'fecha_ingreso', 'fecha_salida', 'estado_visual')
    search_fields = ('rut', 'nombre_visitante')
    list_filter = ('fecha_ingreso', 'fecha_salida')
    actions = [marcar_salida_masiva]

    # Función corregida usando mark_safe
    @admin.display(description="Estado Actual")
    def estado_visual(self, obj):
        if obj.fecha_salida:
            # Usamos mark_safe para decirle a Django: "Este HTML es seguro, dibújalo"
            return mark_safe('<span style="color: gray;">🔴 Finalizada</span>')
        else:
            return mark_safe('<span style="color: green; font-weight: bold;">🟢 En curso</span>')

admin.site.register(Visita, VisitaAdmin)