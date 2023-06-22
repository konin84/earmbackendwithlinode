from django.db import models
from account.models import UserAccount
from autoslug import AutoSlugField

def upload_path(instance, filename):
  return '/'.join(['images/staff_picture', str(instance.staff), filename])  

def upload_logo_path(instance, filename):
  return '/'.join(['images/logo', str(instance.name), filename])
  
def upload_service_path(instance, filename):
  return '/'.join(['images/services', str(instance.name), filename])  

class Company(models.Model):
       
    name = models.CharField(max_length=200)
    mission = models.CharField(max_length=200)
    logo = models.ImageField(upload_to=upload_logo_path, blank=True, null=True)
    vision = models.CharField(max_length=200)
    corevalue = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    facebook_url = models.CharField(max_length=200)
    twitter_url = models.CharField(max_length=200)
    linkedin_url = models.CharField(max_length=200)
    instagram_url = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    class Meta: 
       verbose_name_plural ="company's info"      

    def __str__(self):
      return f'{self.name}'


class CompanyStaff(models.Model):
    
    STAFF_ROLES = [
      ("CEO", "CEO"),
      ("Accountant","Accountant"),
      ("IT", "Head of IT Department")
    ]
     
    staff = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=STAFF_ROLES)
    photo = models.ImageField(upload_to=upload_path, blank=True, null=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title')
    author = models.ForeignKey(UserAccount, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.title
    

class Service(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = AutoSlugField(populate_from='name', null=True, blank=True)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to=upload_service_path, blank=True, null=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ClientService(models.Model):
    client = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

