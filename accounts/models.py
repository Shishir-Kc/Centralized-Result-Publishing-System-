from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Grade(models.Model):
    grade_name = models.CharField(verbose_name="grade_name")

    def __str__ (self):
        return self.grade_name
    

class School(models.Model):
    address = models.CharField(verbose_name='address')
    image = models.ImageField(blank=True,null=True)
    banner = models.ImageField(blank=True,null=True)
    name = models.CharField(verbose_name='School_name')




class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    class is_valid(models.TextChoices):
        ACCEPTED = 'Accepted','Accepted'
        REJECTED = 'Rejected','Rejected'
        PENDING = 'Pending','Pending'

    contact = models.IntegerField(verbose_name='Contact_number',null=True,blank=True)
    account_status = models.CharField(choices=is_valid,verbose_name='Validated ?',max_length=10,default=is_valid.PENDING)
    grade = models.OneToOneField(Grade,blank=True,null=True,on_delete=models.CASCADE)
    registered_school = models.ForeignKey(School,on_delete=models.CASCADE,null=True,blank=True)




    