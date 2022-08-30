from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pid','pname','pcost','pmfdt','pexpdt']
    list_filter = ['pname','pmfdt','pexpdt']
    class meta:
        model = Product
admin.site.register(Product,ProductAdmin)