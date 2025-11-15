from django.urls import path
from tipo_solicitudes import views

'tipo-solicitud/'
urlpatterns = [
    path('', views.agregar, name='agrega_solicitud'),
    path('lista', views.lista_solicitudes, name='lista_tipo_solicitudes'),
    path('crear-formulario', views.crear_formulario, name='crear_formulario'),
    path('formulario/<int:formulario_id>/campos/', views.crear_campos, name='crear_campos'),
    path('formulario/campo/<int:campo_id>/eliminar/', views.eliminar_campo, name='eliminar_campo'),
]
