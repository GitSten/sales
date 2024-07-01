from django.contrib import admin
from .models import Product, Tag, ProductUpdate, News, Information

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'ean', 'retail_price')
    search_fields = ('name', 'code', 'ean')
    filter_horizontal = ('tags',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ProductUpdate)
class ProductUpdateAdmin(admin.ModelAdmin):
    list_display = ('old_product', 'old_code', 'new_product', 'new_code')
    search_fields = ('old_product', 'old_code', 'new_product', 'new_code')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)

@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
