from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimonial, name='testimonial'),
    path('all/', views.testimonial_all, name='testimonial_all'),
]
