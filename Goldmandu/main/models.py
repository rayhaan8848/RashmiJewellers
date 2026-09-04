from django.db import models
from cloudinary.models import CloudinaryField
from django_ckeditor_5.fields import CKEditor5Field


# ==========================================
# OFFER PRODUCT
# ==========================================

class OfferProduct(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    desc = CKEditor5Field(
    'text',
    config_name='extends'
)


    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    image = CloudinaryField('image')

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# ==========================================
# GENDER
# ==========================================

class Gender(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name


# ==========================================
# MATERIAL
# ==========================================

class Material(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name


# ==========================================
# CATEGORY
# ==========================================

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


# ==========================================
# SUBCATEGORY
# ==========================================

class SubCategory(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories"
    )

    name = models.CharField(
        max_length=100
    )

    class Meta:
        unique_together = ('category', 'name')

    def __str__(self):
        return f"{self.category.name} - {self.name}"


# ==========================================
# STONE
# ==========================================

class Stone(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


# ==========================================
# PRODUCT
# ==========================================

class Product(models.Model):

    name = models.CharField(
        max_length=200
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    image = CloudinaryField('image')

    desc = CKEditor5Field(
    'text',
    config_name='extends',
    blank=True,
    default='')

    weight = models.DecimalField(
    max_digits=10,
    decimal_places=3,
    null=True,
    blank=True,
    help_text="Weight in grams"
)

    # ------------------------------
    # RELATIONSHIPS
    # ------------------------------

    gender = models.ForeignKey(
        Gender,
        on_delete=models.PROTECT,
        related_name="products"
    )

    material = models.ForeignKey(
        Material,
        on_delete=models.PROTECT,
        related_name="products"
    )

    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.PROTECT,
        related_name="products"
    )

    stone = models.ForeignKey(
    Stone,
    on_delete=models.PROTECT,
    related_name="products",
    null=True,
    blank=True
)

    # ------------------------------
    # TIMESTAMPS
    # ------------------------------

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name