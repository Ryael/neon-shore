from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('details/', views.profile_details, name='profile_details'),
    path('orders/', views.profile_orders, name='profile_orders'),
    path('account/', views.profile_account, name='profile_account')
]
