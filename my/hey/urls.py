from django.contrib import admin
from django.urls import path
from hey import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('sandwich/', views.sandwich, name='sandwich'),
    path('lasagna/', views.lasagna, name='lasagna'),
    path('pizza/', views.pizza, name='pizza'),
    path('pasta/', views.pasta, name='pasta'),
    path('noodles/', views.noodles, name='noodles'),
    path('cake/', views.cake, name='cake'),
    path('contact/thanks/', views.thanks, name='thanks'),
]