from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
    path('add_wishlist_item/<int:product_id>/', views.add_wishlist_item,
         name='add_wishlist_item'),
    path('delete_wishlist_item/<int:item_id>/', views.delete_wishlist_item,
         name='delete_wishlist_item'),
]
