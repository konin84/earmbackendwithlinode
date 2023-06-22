from django.db import models
from account.models import UserAccount


def upload_path(instance, filename):
  return '/'.join(['images/user_profile', str(instance.accountOwner), filename])  

class Profile(models.Model):
       
    accountOwner = models.OneToOneField(UserAccount, on_delete=models.CASCADE, verbose_name='account owner')
    biography = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to=upload_path, blank=True, null=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    class Meta:
       verbose_name_plural ="Users' Profiles"
    
    def __str__(self):
      return f' profile of {self.accountOwner}'
  

