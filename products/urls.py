from django.contrib import admin
from django.urls import path
from products import views
app_name = 'products'

urlpatterns = [
    path('', views.products, name='index'),
    path('category/<int:category_id>/', views.products, name='category'),
    path('page/<int:page_number>/', views.products, name='paginator'),
    path('basket/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('basket/delete/<int:basket_id>/', views.basket_delete, name='basket_delete'),

]