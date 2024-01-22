from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('biography', views.biography, name='biography'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('what_is_reiki', views.what_is_reiki, name='what_is_reiki'),
]
