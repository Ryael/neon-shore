from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('details/', views.profile_details, name='profile_details'),
    path('orders/', views.profile_orders, name='profile_orders'),
    path('order_history/<order_number>', views.order_history,
         name='order_history'),
    path('account/', views.profile_account, name='profile_account'),
    path('admin/', views.profile_admin, name='profile_admin'),
    path('wishlist/', views.profile_wishlist, name='profile_wishlist')
]
