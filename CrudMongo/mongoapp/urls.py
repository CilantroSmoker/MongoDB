from django.urls import path
from . import views

urlpatterns = [
    path('', views.VehiculoListView.as_view(), name='vehiculo-list'),
    path('crear/', views.VehiculoCreateView.as_view(), name='vehiculo-create'),
    path('<int:pk>/editar/', views.VehiculoUpdateView.as_view(), name='vehiculo-update'),
    path('<int:pk>/eliminar/', views.VehiculoDeleteView.as_view(), name='vehiculo-delete'),
]