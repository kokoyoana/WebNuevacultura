from django.urls import path, include
from .views import *
 
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('inicio/', Index.as_view(), name='inicio'),
    path('asociacion/', Asocia.as_view(), name='asociacion'),
    path('proyectos/', Proyectos.as_view(), name='proyecto'),
    path('infoproyectos/<int:pk>', Infoproyectos.as_view(), name ='infoproyectos'),
    path('contacto/', Contacto.as_view(), name='contactos'),
    path('blog/', Blog.as_view(), name = 'blog'),
    path('infoblog/<int:pk>', InfoBlog.as_view(), name= 'infoblog'),
    path('estatutos/', Datos.as_view(), name= 'datoscontacto'),
    path('aviso/', Datosd.as_view(), name= 'datoscontactod'),
    path('filosofia/', Filo.as_view(), name= 'filosofia'),
    path('talleres/', Talleres.as_view(), name= 'talleres'),
    path('talleres/<int:pk>', Infotalleres.as_view(), name= 'infotalleres'),
]