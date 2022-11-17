from django.urls import path, re_path
from project import views
from django.urls import path, include



from project.views import *
from rest_framework.routers import DefaultRouter


#user_list = UserViewSet.as_view({'get': 'list', 'post':'create'})
#user_detail = UserViewSet.as_view({'get': 'retrieve', 'delete':'destroy', 'put':'update', 'patch':'partial_update'})


product_list = ProductsViewSet.as_view({'get': 'list','post':'create'})
product_detail = ProductsViewSet.as_view({'get': 'retrieve', 'delete':'destroy', 'put':'update', 'patch':'partial_update'})

brand_list = BrandsViewSet.as_view({'get': 'list','post':'create'})
brand_detail = BrandsViewSet.as_view({'get': 'retrieve', 'delete':'destroy', 'put':'update', 'patch':'partial_update'})


router = DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'pro', ProductsViewSet)
router.register(r'br', BrandsViewSet)



urlpatterns = [
   #generics.ListAPIView

    path('users-generic/', UserList.as_view()),
    path('users-generic/<int:pk>/', UserDetail.as_view()), 
    
    path('product/', productlist.as_view(), name="product"),
    path('product/<int:pk>/', productdetail.as_view(), name='product-url'),
    
    path('brand/', Brandlist.as_view(), name='bro'),
    path('brand/<int:pk>/', Branddetail.as_view(), name='brand_id'),
    
    path("get-details",UserDetailAPI.as_view()),
    path('register',RegisterUserAPIView.as_view()),
    path('log/', LoginView.as_view()),
    
    
    #path('user', user_list, name='user-list'),
    #path('user/<int:pk>/', user_detail, name='user-detail'),
    path('',include(router.urls)),
    
    
    path('productvs/',product_list),
    path('productvs/<int:pk>/', product_detail),
    
    
    path('brandvs/',brand_list),
    path('brandvs/<int:pk>/', brand_detail),
    
    path('parser/', ExampleView.as_view()),
    re_path(r'^upload/(<filename>)', FileUploadView.as_view()),
    
    
    path('new/', PurchaseList.as_view())

]

    
