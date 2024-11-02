from django.contrib import admin
from .models import Brand, Car

# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "slug"]
    
class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "slug"]


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)

