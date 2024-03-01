from django.db import models
from django.contrib.auth.models import User
from django.db import models



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self) -> str:
        if self.parent:
            return f"{self.parent.name}  ----- {self.name}"
        return self.name


class SizeCategory(models.Model):
    differens = models.CharField(max_length=100,
                                  verbose_name="O'lcham turi")
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self) -> str:
        return self.differens

    


class Avto(models.Model):
    model = models.CharField(max_length=255)
    size = models.CharField(max_length=200)
    imagess = models.ImageField(upload_to="immdages/")
    brend = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    sizes = models.ForeignKey(SizeCategory, on_delete=models.PROTECT)
    price = models.CharField(max_length=200)
    layer = models.CharField(max_length=200)
    
    


    def __str__(self):
        return self.brend
    


class Cart(models.Model):
    class StatusType(models.TextChoices):
        NEW = 'new', 'Yangi'
        PENDING = 'pending', 'Jarayonda'
        CONFIRMED = 'confirmed', 'Tasdiqlandi'
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.PositiveIntegerField(default=0)
    status = models.CharField(choices=StatusType.choices, default=StatusType.NEW, max_length=100)

    def __str__(self) -> str:
        return f"{self.user} - {self.total_price}"
    

    class Meta:
        verbose_name = "Karzinka"
        verbose_name_plural = 'Karzinkalar'
    

class UserProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='user_products')
    product = models.ForeignKey(Avto, on_delete=models.PROTECT)
    count = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return self.count
    
    class Meta:
        verbose_name = "Foydalanuvchi mahsuloti"
        verbose_name_plural = "Foydalanuvchi mahsulotlari"
    







