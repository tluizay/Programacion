from django.urls import path
from . import views 


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('libros_lista', views.listar_libros, name="libros_lista"),
    path('eliminar_libro/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),
    path('editar_libro/<int:pk>/', views.editar_libro, name='editar_libro'),
    path('detalle_libro/<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('nuevo_libro',views.nuevo_libro, name="nuevo_libro"),
]