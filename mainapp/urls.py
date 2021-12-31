from django.contrib import admin
from django.urls import path
from mainapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainapp'
urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('aboutus',views.about,name="aboutus"),
    path('contact',view=views.contact,name="contact"),
    path('signup',views.signup,name="signup"),
    path("logout", views.logout, name="logout"),
    # path('', views.index, name="user_login"),
]

urlpatterns += staticfiles_urlpatterns()
