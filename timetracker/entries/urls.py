from django.conf.urls import include, url

from entries import views


urlpatterns = [
    url(r'^entries/$', views.entries, name='entries'),
]
