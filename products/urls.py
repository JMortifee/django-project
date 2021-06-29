from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_years, name='portfolio_years'),
    path('media/', views.media, name='media'),
    path('all_works/', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]