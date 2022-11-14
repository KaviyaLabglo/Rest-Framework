from django.urls import path
from project import views
from django.urls import path, include
#from rest_framework.authtoken import views

#from .views import LoginAPI



from project.views import *
#from .views import LoginAPI, RegisterAPI, UserAPI

#from .views import UserAPIView, RegisterAPIView, LoginAPIView



#from rest_framework.authtoken import views



urlpatterns = [
   
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()), 
    
    
    
  
    path('ex/', ExampleView.as_view()),
    path('custom/', CustomAuthToken.as_view()),
    
    
    path('product/', productlist.as_view()),
    path('product/<int:pk>/', productdetail.as_view()),
    
    path("get-details",UserDetailAPI.as_view()),
    path('register',RegisterUserAPIView.as_view()),
    
    path('log/', LoginView.as_view()),

]
    
