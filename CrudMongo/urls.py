from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('vehiculos/', include('mongoapp.urls')),
]