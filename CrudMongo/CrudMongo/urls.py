from django.urls import path, include

urlpatterns = [
    path('vehiculos/', include('mongoapp.urls')),
]