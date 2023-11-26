from django.contrib import admin
from django.urls import path

from products import views
from products.views import ProductsListView

app_name = 'products'

urlpatterns = [
    path('', views.ProductsListView.as_view(), name='index'),
    path('category/<int:category_id>/', views.ProductsListView.as_view(), name='category'),
    path('page/<int:page>/', views.ProductsListView.as_view(), name='paginator'),
    path('basket/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('basket/delete/<int:basket_id>/', views.basket_delete, name='basket_delete'),

]