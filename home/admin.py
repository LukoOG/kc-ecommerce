from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','img','description','date_added']
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','category','slug','price','description','img',
                    'quantity','max_quantity','min_quantity','date_added']
admin.site.register(Product, ProductAdmin)