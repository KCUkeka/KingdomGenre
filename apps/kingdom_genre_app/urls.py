from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^about$', views.about),
    url(r'^sealed_hoodies$', views.sealed_hoodies),
    url(r'^sealed_tshirts$', views.sealed_tshirts),
    url(r'^kingdom_tshirts$', views.kingdom_tshirts),
    url(r'^kingdom_hoodies$', views.kingdom_hoodies),
    url(r'^christ_hoodies$', views.christ_hoodies),
    url(r'^christ_tshirts$', views.christ_tshirts),
    url(r'^contact_us$', views.contact_us),
]