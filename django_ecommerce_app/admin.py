from django.contrib import admin
from .models import *

# Register your models here.
# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('title', 'is_complete', 'time')
#     search_fields = ('title',)
#     list_filter = ('is_complete',)
# # admin.site.register(Task, TaskAdmin)


# @admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    search_fields = ('user',)
admin.site.register(UserProfile, UserProfileAdmin)      # You can either use the decorator above or this...


# @admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name',)
admin.site.register(Product, ProductAdmin)      # You can either use the decorator above or this...

# admin.site.register(UserProfile)
# admin.site.register(Product)
admin.site.register(ProductTag)
admin.site.register(Order)

