from django.urls import path
from . import views

urlpatterns = [
    
    path('add-photo', views.photos),
    path('all-photos', views.allPhoto),
    path('gallery', views.publishedPhotos),
    path('photo/delete/<str:pk>', views.photo),
    path('photo/update/<str:pk>', views.photo),
    path('photo/<str:pk>', views.photo),

]