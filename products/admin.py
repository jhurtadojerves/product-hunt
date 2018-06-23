from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'votes', 'url')
    prepopulated_fields = {'slug': ('title',)}
