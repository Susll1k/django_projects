from django.contrib import admin
from .models import UserProfile, Product

class UserProfileClass(admin.ModelAdmin):
    list_display=('username', 'email')

admin.site.register(UserProfile,UserProfileClass)
admin.site.register(Product)



