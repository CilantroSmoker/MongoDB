from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Vehiculo

class VehiculoListView(ListView):
    model = Vehiculo
    template_name = 'mongoapp/vehiculo_list.html'
    context_object_name = 'vehiculos'

class VehiculoCreateView(CreateView):
    model = Vehiculo
    template_name = 'mongoapp/vehiculo_form.html'
    fields = ['make', 'model', 'price', 'color', 'year', 'status']
    success_url = reverse_lazy('vehiculo-list')

class VehiculoUpdateView(UpdateView):
    model = Vehiculo
    template_name = 'mongoapp/vehiculo_form.html'
    fields = ['make', 'model', 'price', 'color', 'year', 'status']
    success_url = reverse_lazy('vehiculo-list')

class VehiculoDeleteView(DeleteView):
    model = Vehiculo
    template_name = 'mongoapp/vehiculo_confirm_delete.html'
    success_url = reverse_lazy('vehiculo-list')