from django.urls import path
from . import views

urlpatterns = [
     
    path('add-company', views.registeringCompany),
    path('company/<str:pk>', views.companySetting),
    path('company/delete/<str:pk>', views.companySetting),
    path('company/update/<str:pk>', views.companySetting),
    path('company/logo/<str:pk>', views.companyLogoSetting),
    path('company/logo/update/<str:pk>', views.companyLogoSetting),
    
    path('newBlog', views.newBlob),
    path('all-blogs', views.allBlogs),
    path('published-blogs', views.publishedBlogs),
    path('published-blogs/<str:slug>', views.singlePublishedBlog),
    path('blog/<str:slug>', views.blog),
    path('blog/delete/<str:slug>', views.blog),
    path('blog/update/<str:slug>', views.blog),

    path('addService', views.services),
    path('all-services', views.allservices),
    path('service/<str:slug>', views.singleService),
    path('service/update/<str:slug>', views.service),
    path('service/update/image/<str:slug>', views.serviceImageSetting),
    path('service/delete/<str:slug>', views.service),
    path('service/update/image/<str:slug>', views.service),



]