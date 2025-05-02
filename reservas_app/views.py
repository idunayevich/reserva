from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Restaurante, Reserva
from .forms import RestauranteForm, ReservaForm

class RestauranteCreateView(LoginRequiredMixin, CreateView):
    model = Restaurante
    form_class = RestauranteForm
    template_name = 'reservas_app/formulario_restaurante.html'
    success_url = reverse_lazy('restaurante_list')
    
class ReservaCreateView(LoginRequiredMixin, CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservas_app/formulario_reserva.html'
    success_url = reverse_lazy('reserva_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class RestauranteListView(ListView):
    model = Restaurante
    template_name = 'reservas_app/listado_restaurantes.html'

class ReservaListView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = 'reservas_app/listado_reservas.html'
    context_object_name = 'reservas'

