from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('signout', views.signout, name="signout"),
    path('forecast', views.forecast, name="forecast"),
    path('hedge', views.hedge, name="hedge"),
    path('commodityinfo', views.commodityinfo, name="commodityinfo"),
]
