from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Visita
from .forms import VisitaForm
from django.contrib import messages
from django.views.generic import DeleteView

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .serializers import GroupSerializer, UserSerializer, VisitaSerializer


class VisitaViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all().order_by("-fecha_ingreso")
    serializer_class = VisitaSerializer
    permission_classes = [permissions.IsAuthenticated]

# 1. Listar Visitas (Dashboard)
class ListaVisitasView(LoginRequiredMixin, ListView):
    model = Visita
    template_name = 'visitas/lista_visitas.html'
    context_object_name = 'visitas'
    paginate_by = 10

# 2. Registrar Nueva Visita
class CrearVisitaView(LoginRequiredMixin, CreateView):
    model = Visita
    form_class = VisitaForm
    template_name = 'visitas/registro_visita.html'
    success_url = reverse_lazy('lista_visitas')

    # ESTO ES LO NUEVO: Mensaje de éxito
    def form_valid(self, form):
        messages.success(self.request, '¡Visita registrada correctamente!')
        return super().form_valid(form)
    
# Vista para Eliminar
class EliminarVisitaView(LoginRequiredMixin, DeleteView):
    model = Visita
    template_name = 'visitas/eliminar_visita.html'
    success_url = reverse_lazy('lista_visitas')

    def form_valid(self, form):
        messages.success(self.request, 'La visita ha sido eliminada.')
        return super().form_valid(form)

# 3. Marcar Salida (Acción individual desde la vista, no el admin)
def marcar_salida(request, pk):
    visita = Visita.objects.get(pk=pk)
    if not visita.fecha_salida:
        visita.fecha_salida = timezone.now()
        visita.save()
    return redirect('lista_visitas')

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]