from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
    path('favourite/<int:product_id>/', views.favourite_product,
         name='favourite_product'),
    path('fav_products/', views.fav_products_list, name='fav_products'),
    path('deactivate/', views.deactivate_account, name='deactivate_account'),
]
