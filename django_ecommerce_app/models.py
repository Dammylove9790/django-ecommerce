from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class UserLogin(models.Model):
    

class UserProfile(models.Model):
    user =   models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, null=True)
    image = models.ImageField( default='default.jpg', upload_to='profile_pics', height_field=None, width_field=None, max_length=None)
    is_active = models.BooleanField(default=False, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f'{self.user.username} Profile'



class ProductTag(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return self.name



class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )

    name = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=50, null=True, choices=CATEGORY)
    description = models.TextField(max_length=225, blank=True, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(ProductTag)
    
    def __str__(self) -> str:
        return self.name



class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)
    
    def __str__(self):
        return f'{self.user.username} order'


