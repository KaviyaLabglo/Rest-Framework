from django.urls import path
from project import views
from django.urls import path, include



from project.views import *


urlpatterns = [
   
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()), 
    
    
    
  
    
    
    
    path('product/', productlist.as_view()),
    path('product/<int:pk>/', productdetail.as_view()),
    
    path("get-details",UserDetailAPI.as_view()),
    path('register',RegisterUserAPIView.as_view()),
    
    path('log/', LoginView.as_view()),

]
    
