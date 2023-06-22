from django.contrib import admin
from .models import Company, CompanyStaff, BlogPost, Service, ClientService
# Register your models here.

admin.site.register(Company)
admin.site.register(CompanyStaff)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogPost)
admin.site.register(Service)
admin.site.register(ClientService)