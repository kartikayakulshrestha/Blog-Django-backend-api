from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# creating blog model here
class User(models.Model):
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    email=models.EmailField(max_length=60,unique=True)
    password=models.CharField(max_length=40)
    create_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname+" "+self.lastname


class Blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now=True)
    

class likes(models.Model):
    create_at=models.DateTimeField(auto_now=True)
    blog_id=models.ForeignKey(Blog,on_delete=models.CASCADE)
    liker_id=models.ForeignKey(User,on_delete=models.CASCADE)


class comments(models.Model):
    create_at=models.DateTimeField(auto_now=True)
    blog_id=models.ForeignKey(Blog,on_delete=models.CASCADE)
    commenter_id=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.CharField(max_length=500)

# version2    
class userV2(models.Model):
    user=models.ForeignKey(AbstractUser,on_delete=models.CASCADE)

#write a code to manage the model in the admin panel



