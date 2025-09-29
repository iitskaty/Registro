from django.urls import path
from . import views
urlpatterns = [
    path("", views.lista_visitas, name="lista_visitas"),
    path("Sistema/<int:id>/", views.detalle_visita, name="detalle_visita"),
    path("Sistema/nuevo/", views.nueva_visita, name="nueva_visita"),
    path("Sistema/editar/<int:id>/", views.editar_visita, name="editar_visita"),
    path("Sistema/eliminar/<int:id>/", views.eliminar_visita, name="eliminar_visita"),
]