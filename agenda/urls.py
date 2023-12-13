from django.urls import path
from .views import EventoLista, EventoDetalle

urlpatterns = [
    path('eventos/', EventoLista.as_view(), name='evento-lista'),
    path('eventos/<int:pk>/', EventoDetalle.as_view(), name='evento-detalle'),
]