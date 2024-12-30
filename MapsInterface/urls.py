from django.contrib import admin
from django.urls import path
from apps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inscription, name='inscription'),
    path('login/', views.login, name='login'),
    path('acceuil/', views.acceuil, name='acceuil'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logout, name='logout'),




]

