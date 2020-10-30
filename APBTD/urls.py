from django.contrib import admin
from django.urls import path,re_path,include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('',include('apps.main.urls')),
    re_path('',include('apps.juegos.urls')),
    re_path('',include('apps.operadores.urls')),
    re_path('',include('apps.sistemas_ecuaciones.urls')),
    re_path('',include('apps.logica_predicados.urls')),
    re_path('',include('apps.teoria_conjuntos.urls')),
    re_path('',include('apps.diagramas_flujo.urls')),
    re_path('',include('apps.vectores.urls')),
    re_path('',include('apps.matrices.urls')),
    re_path('',include('apps.precedencia_operadores.urls')),
    re_path('',include('apps.razonamiento_abstracto.urls')),
    re_path('',include('apps.razonamiento_inductivo.urls')),
    re_path('',include('apps.razonamiento_deductivo.urls')),
    re_path('',include('apps.funciones.urls')),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
