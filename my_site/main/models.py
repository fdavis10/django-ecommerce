from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField
    

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=250, db_index=True, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering=('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        pass

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.CharField(max_length=150, db_index=True)
    image = models.FileField(blank=True, upload_to='pass')

    SIZE_PRODUCT = (
        ('SMALL', 'SMALL'),
        ('MIDDLE', 'MIDDLE'),
        ('LARGE', 'LARGE'),
        ('SUPERLARGE', 'SUPER-LARGE'))
    
    size = MultiSelectField(choices=SIZE_PRODUCT, max_choices=4, max_length=50)
    description = models.TextField(max_length=250, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
        
    class Meta:
            verbose_name = "Product"
            verbose_name_plural = "Products"
            ordering = ('name',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass
            
