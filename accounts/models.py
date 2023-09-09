from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class address(models.Model):
    name = models.CharField(max_length=255, null= True, blank=True)
    city = models.CharField(max_length=255, null= True, blank=True)
    province = models.CharField(max_length=255, null= True, blank=True)
    full = models.CharField(max_length=255, null= True, blank = True)
    post_code = models.CharField(max_length=255, null= True, blank = True)
    reciever = models.CharField(max_length=255, null= True, blank = True)
    phone = models.CharField(max_length=11, null= True, blank = True)

    def __str__(self):
        return self.name


class CustumUser(AbstractUser):
    image = models.ImageField(upload_to='user', default='user.png')
    cell_phone = models.CharField(max_length=11, null= True, blank=True)
    tell_phone = models.CharField(max_length=11, null= True, blank=True)
    birthdata = models.DateField(null=True, blank=True)
    melicode = models.CharField(max_length=10, null= True, blank = True)
    credit_number = models.CharField(max_length=16, null= True, blank=True)

    def __str__(self):
        return self.username
# Create your models here.
