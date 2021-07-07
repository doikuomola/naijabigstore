from autoslug import AutoSlugField
from django.conf import global_settings as settings
from django.db import models
from django.db.models.fields import SlugField
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('store:product_list_by_category', args=[self.slug])


class TopCategory(models.Model):
    top_categories = models.ForeignKey(
        Category, related_name="topcategories", on_delete=models.CASCADE)
    top_category_icon = models.ImageField(upload_to="media/topcategoryicon")

    class Meta:
        verbose_name = 'TopCategory'
        verbose_name_plural = 'TopCategories'


class TopBrand(models.Model):
    top_brand_logo = models.ImageField(upload_to="media/topbrandslogo")

    class Meta:
        verbose_name = 'TopBrand'
        verbose_name_plural = 'TopBrands'


class Seller(models.Model):
    seller_name = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    platform_description = models.TextField()
    platform_logo = models.ImageField(blank=True, null=True)
    customized_name = AutoSlugField(populate_from='seller_name', max_length=50)

    class Meta:
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'

    def __str__(self):
        return self.seller_name.username


class Product(models.Model):
    seller_name = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True)
    thumbnail = models.ImageField(
        upload_to="media/selleritem", blank=True, null=True)
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    featured = models.BooleanField(default=False)
    flash_deal = models.BooleanField(default=False)
    flash_deal_end_date = models.DateTimeField()
    flash_deal_date_created = models.DateTimeField(auto_now_add=True)
    most_viewed = models.BooleanField(default=False)
    recommended = models.BooleanField(default=False)
    deal = models.BooleanField(default=False)
    deal_available_quantity = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.id, self.slug])