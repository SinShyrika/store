from django.contrib import admin

from products.models import Basket, Product, ProductCategory


@admin.register(Product)
class Product_admin(admin.ModelAdmin):
    list_display = ('name','price','quantity','category')
    fields = ('name','description',('price','quantity'),'image','stripe_product_basket_id', 'category')
    search_fields = ('name','description')
    ordering =('name',)

@admin.register(ProductCategory)
class Product_category_admin(admin.ModelAdmin):
    list_display = ('name','description')
    fields = ('name','description')
    search_fields = ('name','description')
    ordering =('name',)

class Basket_admin(admin.TabularInline):
    model = Basket
    fields = ('products','quantity')
