from django.contrib import admin
from .models import (
    OfferProduct,
    Gender,
    Material,
    Category,
    SubCategory,
    Stone,
    Product,
)


# ==========================================
# OFFER PRODUCT
# ==========================================

@admin.register(OfferProduct)
class OfferProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'name',
        'price',
        'is_active',
        'created_at',
    )

    list_filter = (
        'is_active',
        'created_at',
    )

    search_fields = (
        'title',
        'name',
        'desc',
    )


# ==========================================
# GENDER
# ==========================================

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# ==========================================
# MATERIAL
# ==========================================

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# ==========================================
# CATEGORY
# ==========================================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# ==========================================
# SUBCATEGORY
# ==========================================

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
    )

    list_filter = (
        'category',
    )

    search_fields = (
        'name',
        'category__name',
    )


# ==========================================
# STONE
# ==========================================

@admin.register(Stone)
class StoneAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# ==========================================
# PRODUCT
# ==========================================

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'price',
        'gender',
        'material',
        'subcategory',
        'stone',
        'created_at',
    )

    list_filter = (
        'gender',
        'material',
        'subcategory__category',
        'subcategory',
        'stone',
        'created_at',
    )

    search_fields = (
        'name',
        'description',
        'gender__name',
        'material__name',
        'subcategory__name',
        'subcategory__category__name',
        'stone__name',
    )

    list_per_page = 25