from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100, unique=True)
    ean = models.CharField(max_length=13, unique=True)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    info_url = models.URLField()
    image = models.ImageField(upload_to='products/')
    imageorig = models.ImageField(upload_to='products/')
    tags = models.ManyToManyField(Tag, blank=True)  # Added this field

    def __str__(self):
        return self.name


class ProductUpdate(models.Model):
    old_product = models.CharField(max_length=255, blank=True, null=True)
    old_code = models.CharField(max_length=100, blank=True, null=True)
    old_ean = models.CharField(max_length=13, blank=True, null=True)
    old_image = models.ImageField(upload_to='product_updates/', blank=True,)
    new_product = models.CharField(max_length=255, blank=True, null=True)
    new_code = models.CharField(max_length=100, blank=True, null=True)
    new_ean = models.CharField(max_length=13, blank=True, null=True)
    new_image = models.ImageField(upload_to='product_updates/', blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.old_product if self.old_product else 'Product Update'



class News(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text



class Information(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()  # Sisestage HTML-sisu

    def __str__(self):
        return self.title
