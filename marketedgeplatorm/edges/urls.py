from django.contrib import admin

from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.edges, name="edges-home"),
    path('daily-odds', views.daily_odds, name="daily-odds"),

]