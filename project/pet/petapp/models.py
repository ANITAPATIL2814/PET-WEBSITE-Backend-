from django.db import models

class Pet(models.Model):
    CAT=((1,'Dog'),(2,'Cat'),(3,'Bird'))
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image')
    description = models.TextField()
    price = models.IntegerField()
    life = models.IntegerField(help_text='Life in months')
    color = models.CharField(max_length=50)
    cat= models.IntegerField(choices=CAT) 
    is_active = models.BooleanField(default=True)

from django.contrib.auth.models import User 
class petcart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey(Pet,on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)

class order(models.Model):
    order_id=models.CharField(max_length=50)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey(Pet,on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)