from django.contrib import admin
from user.models import User
from products.admin import Basket_admin

@admin.register(User)
class User_admin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (Basket_admin,)
    extra = 0



