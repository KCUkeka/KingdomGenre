from django.conf.urls import url, include 
# from django.contrib import admin 

urlpatterns = [
    url(r'^', include('apps.kingdom_genre_app.urls')),
    # url(r'^admin/', admin.sites.urls), 
]