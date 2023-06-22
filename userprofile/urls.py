from django.urls import path
from . import views

urlpatterns = [ 
      path('profile', views.profileSetting),
      path('update/<str:pk>', views.userProfile),
      path('myProfile', views.MyProfile.as_view()),
 ]

