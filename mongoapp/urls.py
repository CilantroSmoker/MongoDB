from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.vehiculo_list, name='vehiculo-list'),
    path('cliente/', views.vehiculo_cliente, name='vehiculo-cliente'),
    path('crear/', views.vehiculo_create, name='vehiculo-create'),
    path('<str:pk>/editar/', views.vehiculo_update, name='vehiculo-update'),
    path('<str:pk>/eliminar/', views.vehiculo_delete, name='vehiculo-delete'),
]