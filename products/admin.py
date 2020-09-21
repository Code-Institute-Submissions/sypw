from django.contrib import admin
from .models import Product, Payslip

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "price",
        "additional_info",
    )

    ordering = ("pk",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Payslip)
