from django.conf.urls import url
from django.contrib import admin
from boletin import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^$', views.inicio, name="inicio"),
]
