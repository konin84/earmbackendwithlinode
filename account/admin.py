from django.contrib import admin
from .models import UserAccount, Administrator, Client

# Register your models here.

admin.site.register(UserAccount)
admin.site.register(Administrator)
admin.site.register(Client)
