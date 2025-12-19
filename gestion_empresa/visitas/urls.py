from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaVisitasView.as_view(), name='lista_visitas'),
    path('nueva/', views.CrearVisitaView.as_view(), name='crear_visita'),
    path('salida/<int:pk>/', views.marcar_salida, name='marcar_salida'),
    path('eliminar/<int:pk>/', views.EliminarVisitaView.as_view(), name='eliminar_visita'),
]