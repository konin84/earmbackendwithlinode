from django.urls import path
from . import views

urlpatterns = [
    
  path('administratorSignup', views.SignUpAdministrator.as_view()),
  
  path('clientSignup', views.ClientSignUp.as_view()),
  # path('agentUsers', views.AgentCreatedUsers.as_view()),
  # Strickly for admin
  # view-users
  path('listUsers', views.allUsers),
  path('clients', views.allClients),
  path('client/<str:pk>', views.client),


]