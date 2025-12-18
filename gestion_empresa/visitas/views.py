from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Visita
from .forms import VisitaForm

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

# 3. Marcar Salida (Acción individual desde la vista, no el admin)
def marcar_salida(request, pk):
    visita = Visita.objects.get(pk=pk)
    if not visita.fecha_salida:
        visita.fecha_salida = timezone.now()
        visita.save()
    return redirect('lista_visitas')