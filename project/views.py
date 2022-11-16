from .serializers import UserSerializer, RegisterSerializer
from project.models import *
from rest_framework import views
from django.contrib.auth import login
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from .serializers import ProductSerializer
from rest_framework import mixins
from project.serializers import *
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

#for filter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Generic APIview
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']
    
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['username', 'email']
    ordering = ['username']

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_class = ['brand_name']
    
    
    
from rest_framework import viewsets
from rest_framework.decorators import action, renderer_classes
from rest_framework import permissions, renderers, viewsets
from django.shortcuts import get_object_or_404

from rest_framework import filters

class ProductsViewSet(viewsets.ViewSet):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    
    def list(self, request):
        print(request.method)
        print(self.request.query_params)
        queryset =  product.objects.all()
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    
    def retrieve(self, request, pk=None):
        queryset =  product.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(user, context={'request': request})
        return Response(serializer.data)



    def destroy(self, request, pk=None):
        d = product.objects.filter(id=pk).delete()
        print(d)
        serializer = ProductSerializer(self.request.user)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        
    def update(self, request, pk= None):
        user_obj =  product.objects.get(id=pk)
        serializer = ProductSerializer(user_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def partial_update(self, request, pk= None):
        user_obj = product.objects.get(id=pk)
        serializer = ProductSerializer(user_obj, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        

class BrandsViewSet(viewsets.ViewSet):
    queryset =  Brand.objects.all()
    serializer_class =  BrandSerializer
    def list(self, request):
        queryset =  Brand.objects.all()
        serializer = BrandSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    
    def retrieve(self, request, pk=None):
        queryset =   Brand.objects.all()
        user = get_object_or_404(queryset, pk=pk,)
        serializer =  BrandSerializer(user, context={'request': request})
        return Response(serializer.data)



    def destroy(self, request, pk=None):
        d =  Brand.objects.filter(id=pk).delete()
        print(d)
        serializer =  BrandSerializer(self.request.user)
        return Response(serializer.data)
    
    def create(self, request):
        serializer =  BrandSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        
    def update(self, request, pk= None):
        user_obj =   Brand.objects.get(id=pk)
        serializer = BrandSerializer(user_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def partial_update(self, request, pk= None):
        user_obj = Brand.objects.get(id=pk)
        serializer = BrandSerializer(user_obj, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

#mixin
class productlist(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = product.objects.all()
    #filter_backends = [filters.SearchFilter]
   # search_class = ['brand_name']
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields =  ["brand"]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'id']
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   
 
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class productdetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        print(self.request.query_params)
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView


#Generic ListCreate and Generic RetrieveUpdateDestroy APIView
class Brandlist(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    #parser_classes = [JSONParser]
    serializer_class = BrandSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields =  ["brand_name",'id']
  

class Branddetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class UserDetailAPI(APIView):
  
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):

        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

# Class based view to register user


class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginView(views.APIView):
    
    authentication_classes = (TokenAuthentication,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        

from rest_framework import viewsets
from rest_framework.decorators import action, renderer_classes
from rest_framework import permissions, renderers, viewsets
from django.shortcuts import get_object_or_404

from rest_framework import filters

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)



    def destroy(self, request, pk=None):
        d = User.objects.filter(id=pk).delete()
        print(d)
        serializer = UserSerializer(self.request.user)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        
    def update(self, request, pk= None):
        user_obj = User.objects.get(id=pk)
        serializer = UserSerializer(user_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def partial_update(self, request, pk= None):
        user_obj = User.objects.get(id=pk)
        serializer = UserSerializer(user_obj, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
''' 
class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = product.objects.all()
    serializer_class = ProductSerializer

class BrandViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer'''
    
    
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    parser_classes = [JSONParser]
    

    def post(self, request, format=None):
        print(type(request.data))
        print(request.content_type)
        print(request.stream)
        return Response({'received data': request.data})
    
class FileUploadView(views.APIView):
    parser_classes = [FileUploadParser]

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)
        
    