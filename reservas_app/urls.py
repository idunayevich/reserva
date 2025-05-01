from django.urls import path
from .views import RestauranteCreateView, ReservaCreateView,RestauranteListView, ReservaListView
from . import views

urlpatterns = [
    path('nueva/', ReservaCreateView.as_view(), name='reserva_create'),
    path('', ReservaListView.as_view(), name='reserva_list'),
    path('restaurantes/', RestauranteListView.as_view(), name='restaurante_list'),
    path('restaurantes/nuevo/', RestauranteCreateView.as_view(), name='restaurante_create'),
]