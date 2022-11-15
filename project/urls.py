from django.urls import path
from project import views
from django.urls import path, include



from project.views import *
from rest_framework.routers import DefaultRouter
user_list = UserViewSet.as_view({'get': 'list',
                                 'post':'create'})
#user_list = UserViewSet.as_view({'post': 'create',})

user_detail = UserViewSet.as_view({'get': 'retrieve', 'delete':'destroy', 'put':'update', 'patch':'partial_update'})

router = DefaultRouter()
router.register(r'users',UserViewSet,basename="user")



urlpatterns = [
   #generics.ListAPIView
   
    path('users-generic/', UserList.as_view()),
    path('users-generic/<int:pk>/', UserDetail.as_view()), 
    
    path('product/', productlist.as_view()),
    path('product/<int:pk>/', productdetail.as_view()),
    
    path("get-details",UserDetailAPI.as_view()),
    path('register',RegisterUserAPIView.as_view()),
    
    path('log/', LoginView.as_view()),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    #path('',include(router.urls)),

]

    
