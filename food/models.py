from audioop import reverse
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# Create your models here.
class Item(models.Model):

    def __str__(self):          #this will format the output in our pythom shell database in order to se the actual object name
        return self.item_name

    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name= models.CharField(max_length=200)
    item_desc= models.CharField(max_length=200)
    recipe = models.TextField(max_length=2000)#recepie field
    item_image = models.CharField(max_length=500,default="https://th.bing.com/th/id/OIP.ISK0kbvLUbQTc9hltD47fAHaF0?pid=ImgDet&rs=1")

    def get_absolute_url(self):
        return reverse("food:detail",kwargs={"pk":self.pk})