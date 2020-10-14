from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "price",
        "additional_info",
    )

    ordering = ("pk",)


admin.site.register(Product, ProductAdmin)
