
from django.urls import path
from . import views

app_name= 'clientes'

urlpatterns = [
    path('', views.lista, name ='lista'),
    path( 'crear/', views.crear, name = 'crear'),
    path('editar/<int:Id_Cliente>/',
        views.editar,
        name = 'editar'
    ),
    path(
        'desactivar/<int:pk>/', 
        views.desactivar_cliente,
        name='desactivar'
    ),
]





