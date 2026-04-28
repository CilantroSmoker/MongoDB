from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehiculo_list, name='vehiculo-list'),
    path('crear/', views.vehiculo_create, name='vehiculo-create'),
    path('<str:pk>/editar/', views.vehiculo_update, name='vehiculo-update'),
    path('<str:pk>/eliminar/', views.vehiculo_delete, name='vehiculo-delete'),
]