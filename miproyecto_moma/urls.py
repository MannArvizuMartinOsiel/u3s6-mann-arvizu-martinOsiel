# admin: panel de administración de Django
from django.contrib import admin
# path: función para definir rutas
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
]