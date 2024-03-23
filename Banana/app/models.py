from django.db import models

# Create your models here.
class Carousel(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=10000, blank=False)
    image = models.ImageField(upload_to='carousel_background',blank=False)

    def __str__(self) :
        return self.title

class Interior_products(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=10000, blank=False)
    image = models.ImageField(upload_to='Interior_product_images',blank=False)

    def __str__(self) :
        return self.title
    
class Exterior_products(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=10000, blank=False)
    bullet_points = models.TextField(max_length=500, blank=False)
    image = models.ImageField(upload_to='Exterior_product_images',blank=False)

    def __str__(self) :
        return self.title
    
class Base_paint_products(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=10000, blank=False)
    bullet_points = models.TextField(max_length=500, blank=False)
    image = models.ImageField(upload_to='Base_paint_product_images',blank=False)

    def __str__(self) :
        return self.title
    
class Blogs(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=10000, blank=False)
    image = models.ImageField(upload_to='Blogs_images',blank=False)
    date_time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True)

    def __str__(self) :
        return self.title
    
class Colors(models.Model):
    STD_NAME = models.CharField(max_length=100,blank=False)
    NAME = models.CharField(max_length=100,blank=False)
    COLOR_CODE = models.CharField(max_length=10,blank=False)
    R = models.IntegerField(blank=False)
    G = models.IntegerField(blank=False)
    B = models.IntegerField(blank=False)

    def __str__(self) :
        return self.NAME,self.COLOR_CODE
    
class Contacts(models.Model):
    
    first_name=models.CharField(max_length=50, blank=False)
    last_name=models.CharField(max_length=50, blank=False)
    mbl_no=models.IntegerField(blank=False)
    pincode=models.SmallIntegerField(blank=False)
    email=models.EmailField(blank=False)
    adress=models.TextField(max_length=500, blank=True)
    other_query=models.CharField(max_length=50,blank=True)
    paint_choice=models.CharField(max_length=50,blank=True)
    service_choice=models.CharField(max_length=50,blank=True)
    message=models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.first_name
