from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField

# Create your models here.

class Division(models.Model):
    Name = models.CharField(max_length=250)
    def __str__(self):
        return self.Name

class District(models.Model):
    Name = models.CharField(max_length=250)
    Division = models.ForeignKey("Division", on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.Name

class Category(models.Model):
    Name = models.CharField(max_length=250)
    Image = models.ImageField(upload_to='pictures',null = True)
    def __str__(self):
        return self.Name

class Advertisement(models.Model):
    Book_Name = models.CharField( max_length=250)
    Authors_Name = models.CharField(max_length=250)
    Category = models.ForeignKey("Category",on_delete=models.CASCADE,null=True)
    Books_Condition = models.BooleanField(default=False, null=True)
    Location = models.CharField(max_length=250)
    Division = models.ForeignKey("Division", on_delete=models.CASCADE,null=True)
    Details = models.TextField()
    Price = models.IntegerField()
    Image = models.ImageField(
        upload_to='pictures',
        height_field=None,
        width_field=None,
        max_length=None,
        null = True,
        )
    Poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True)
    def __str__(self):
        return self.Book_Name+"-"+self.Poster.first_name
    

# adding str method to User model
def get_name(self):
    return self.first_name+" "+self.last_name
User.add_to_class("__str__", get_name)


class Profile(models.Model):
    Image = models.ImageField(upload_to="pictures",null = True)
    Division = models.ForeignKey("Division", on_delete=models.CASCADE)
    District = models.ForeignKey("District", on_delete=models.CASCADE)
    Phone = models.CharField(max_length=20)
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.User.first_name+" "+self.Phone