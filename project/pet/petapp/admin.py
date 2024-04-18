from django.contrib import admin 
from .models import Pet

# Register your models here.
#admin.site.register(product)

# list display
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','description','price','life','color','cat','is_active']
    #filter 
    list_filter=['cat','is_active']
admin.site.register(Pet,ProductAdmin)
