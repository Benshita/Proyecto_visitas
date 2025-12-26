from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"visitas", views.VisitaViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('', views.ListaVisitasView.as_view(), name='lista_visitas'),
    path('nueva/', views.CrearVisitaView.as_view(), name='crear_visita'),
    path('salida/<int:pk>/', views.marcar_salida, name='marcar_salida'),
    path('eliminar/<int:pk>/', views.EliminarVisitaView.as_view(), name='eliminar_visita'),
]