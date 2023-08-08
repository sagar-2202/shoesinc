from django.db import models

# Create your models here.
# class pinfo(models.Model):
#     name=models.CharField(max_length=122)
#     email=models.CharField(max_length=122)
#     phone=models.CharField(max_length=12)
#     desc=models.TextField()

#     def __str__(self):
#         return self.name
    
class personinfo(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()

    def __str__(self):
        return self.name
    
class signInfo(models.Model):
    username=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    