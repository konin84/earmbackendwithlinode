from django.urls import path
from . import views
# from .views import TestView
from .views import MyTokenObtainPairView


from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('', views.getRoutes),
    path('login/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
   
]
     
