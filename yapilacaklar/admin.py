from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'slug')

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'slug')

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)

admin.site.register(ToDo)