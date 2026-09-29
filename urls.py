# path: función para definir una ruta individual
from django.urls import path
# views: el archivo que acabás de escribir, en la misma carpeta
from . import views

# urlpatterns: lista de rutas que esta app entiende
urlpatterns = [
    # '': la URL vacía (la raíz de esta app) · views.inicio: la función que la atiende
    # name='inicio': un alias interno para referirse a esta ruta sin escribir la URL a mano
    path('', views.inicio, name='inicio'),
]
# admin: ya viene importado por defecto, no lo borres
from django.contrib import admin
# path, include: include permite delegar un grupo de rutas a otra app
from django.urls import path, include

urlpatterns = [
    # ruta del panel de administración, ya incluida por defecto
    path('admin/', admin.site.urls),
    # '': todo lo que llegue a la raíz del sitio se delega a core/urls.py
    path('', include('core.urls')),
]