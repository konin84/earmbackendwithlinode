from django.db import models

def upload_path(instance, filename):
  return '/'.join(['gallery/photos', str(instance.occasion), filename])  

   
class Photo(models.Model):
    occasion = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to=upload_path, blank=True, null=True)
    description = models.TextField(max_length=200,   null=False, blank=False)
    published = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.occasion
