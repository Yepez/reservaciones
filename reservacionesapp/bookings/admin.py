from django.contrib import admin
from .models import Category, Product, Purchase, PurchaseDetail, Sale, SaleDetail, Store


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'description', 'price', 'available', 'category', 'status', 'created_at')


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'total', 'created_at')


class PurchaseDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'purchase_id', 'product_id', 'price', 'quantity', 'subtotal')


class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'total', 'created_at')


class SaleDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'sale_id', 'product_id', 'price', 'quantity', 'subtotal')


class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'price', 'quantity')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PurchaseDetail, PurchaseDetailAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(SaleDetail, SaleDetailAdmin)
admin.site.register(Store, StoreAdmin)