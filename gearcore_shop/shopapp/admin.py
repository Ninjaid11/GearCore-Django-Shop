from django.contrib import admin
from .models import Product, Brand, Category, Tag, Comment


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'in_stock', 'brand', 'category', 'is_top')
    list_filter = ('brand', 'category', 'is_top', 'in_stock')
    search_fields = ('name', 'description')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'content', 'created_at')
    search_fields = ('user__username', 'product__name', 'content')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)