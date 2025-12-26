from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"visitas", views.VisitaViewSet)

urlpatterns = [
    # --- CAMBIO IMPORTANTE AQUÍ ABAJO ---
    # Le ponemos "api/" al principio para que no choque con tu web
    path("api/", include(router.urls)), 
    
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),

    # --- TU PÁGINA WEB ---
    # Ahora sí, al estar vacía "", esta línea será la dueña de la portada
    path('', views.ListaVisitasView.as_view(), name='lista_visitas'),
    
    path('nueva/', views.CrearVisitaView.as_view(), name='crear_visita'),
    path('salida/<int:pk>/', views.marcar_salida, name='marcar_salida'),
    path('eliminar/<int:pk>/', views.EliminarVisitaView.as_view(), name='eliminar_visita'),
]