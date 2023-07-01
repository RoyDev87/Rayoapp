from django.urls import path
from rayoapp import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [

    path('', views.inicio, name='inicio'),
    path('paginas/mecanico', views.mecanico, name='jorge'),
    path('mecanicos/crear', views.crearmec, name='crear'),
    path('mecanicos/editar/<int:id>', views.editarmec, name='editar'),
    path('eliminar/<int:id>', views.eliminarmec, name='eliminar')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
