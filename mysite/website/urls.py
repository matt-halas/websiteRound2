from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('fluidSim', views.fluidSim, name='fluidSim'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('resume', views.resume, name='resume'),
    path('<str:projectTitle>', views.projectView, name='projectView')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
