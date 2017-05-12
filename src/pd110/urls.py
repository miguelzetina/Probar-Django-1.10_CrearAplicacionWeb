from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from boletin import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^$', views.inicio, name="inicio"),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)