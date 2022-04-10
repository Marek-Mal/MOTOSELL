from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import MotoSellModel, MemberMotoSell
from .serializers import MotoSellSerializer, MyAuthTokenSerializer
from django.core.files.storage import default_storage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from rest_framework import viewsets, permissions, parsers, renderers, generics, mixins
from .serializers import UserSerializer, MotoSellSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import obtain_auth_token, ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser

# User Post Methods
class getmoto(viewsets.ModelViewSet):
    queryset = MotoSellModel.objects.all()
    serializer_class = MotoSellSerializer
    authentication_classes = ()
    http_method_names = ['get']

class postmoto(viewsets.ModelViewSet):
    queryset = MotoSellModel.objects.all()
    serializer_class = MotoSellSerializer
    parser_class = (FileUploadParser,)
    permission_classes = [IsAuthenticated,]
    http_method_names = ['post']

    def list(self, request, *args, **kwargs):

      print('='*30)
      print(request.user)
      print('='*30)
      file_serializer = MotoSellSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data)
      else:
          return Response(file_serializer.errors)

class putmoto(generics.UpdateAPIView):
    queryset = MotoSellModel.objects.all()
    serializer_class = MotoSellSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['put']

class deletemoto(generics.DestroyAPIView):
    queryset = MotoSellModel.objects.all()
    serializer_class = MotoSellSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['delete']

#END USER POST METHODS


# USER

class sort(viewsets.ModelViewSet):
    queryset = MotoSellModel.objects.all()
    serializer_class = MotoSellSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request, *args, **kwargs):
        queryset = MotoSellModel.objects.filter(post_Moto=request.user)
        json = MotoSellSerializer(queryset, many=True).data
        return Response(json)

class users(viewsets.ModelViewSet):
    queryset = MemberMotoSell.objects.all()
    serializer_class = UserSerializer
    authentication_classes = ()
    http_method_names = ['get', 'post']


class currentuser(viewsets.ModelViewSet):
    queryset = MemberMotoSell.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    def list(self, request, *args, **kwargs):
        val = {
            "username": request.user.username,
            "surname": request.user.surname,
            "email": request.user.email,
            "user_id": request.user.user_id,
        }
        return Response(val)
    
class updateuser(generics.UpdateAPIView):
    queryset = MemberMotoSell.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['put']
    
class deleteuser(generics.DestroyAPIView):
    queryset = MemberMotoSell.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['delete']

#END USERS

class Myobtain_auth_token(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = MyAuthTokenSerializer
    authentication_classes = ()

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email",
                        description="Valid Email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': UserSerializer(user).data})

        

