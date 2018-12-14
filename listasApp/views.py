from .models import Lista, Producto, User
from rest_framework import viewsets, permissions, generics
from listasApp.serializers import ListaSerializer, ProductoSerializer,LoginUserSerializer,UserSerializer, CreateUserSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from knox.models import AuthToken
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView

class ListaViewSet( viewsets.ModelViewSet ):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ListaSerializer

    def get_queryset(self):
        return self.request.user.lista.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductoViewSet( viewsets.ModelViewSet ):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })
