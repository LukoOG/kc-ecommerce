from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug =  models.SlugField(default="")
    img = models.ImageField(default='category.img', upload_to="Category")
    description = models.TextField(max_length=255)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    slug = models.SlugField(default="")
    quantity = models.IntegerField()
    img = models.ImageField(default='product.jpg', upload_to="Product")
    price = models.IntegerField()
    max_quantity = models.IntegerField()
    min_quantity = models.IntegerField()
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name} --- {self.category.name}"