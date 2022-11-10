from django.urls import include, path
from rest_framework import routers
from project import views
from project.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
'''router = routers.SimpleRouter()
router.register(r'accounts', views.AccountViewSet)'''


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', TodoListApiView.as_view()),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view())
]

#from django.conf.urls import url
#from django.urls import path, include
#from .views import (
   # TodoListApiView,
#)


