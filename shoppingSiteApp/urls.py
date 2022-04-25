from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #re_path(r'^tagged/?P<tag>\D+', views.tagged, name='tagged'),
    re_path(r'^tagged/(?P<tag>\w+)/$', views.tagged, name='tagged'),




]
