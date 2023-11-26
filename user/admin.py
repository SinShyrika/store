from django.contrib import admin

from products.admin import Basket_admin
from user.models import EmailVerification, User


@admin.register(User)
class User_admin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (Basket_admin,)
    extra = 0

@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code','user','expiration')
    fields = ('code','user','expiration','created')
    readonly_fields = ('created',)



