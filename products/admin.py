from django.contrib import admin

from .models import Product


class VotesInline(admin.StackedInline):
    model = Product.votes.through
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'url',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        VotesInline,
    ]


