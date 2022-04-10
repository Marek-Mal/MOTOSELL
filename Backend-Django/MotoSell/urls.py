from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework import routers
from .models import MemberMotoSell
from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from rest_framework.authtoken.views import obtain_auth_token, ObtainAuthToken
from .views import Myobtain_auth_token, updateuser, postmoto, putmoto, getmoto, deletemoto, sort, currentuser, deleteuser
from rest_framework.authtoken.serializers import AuthTokenSerializer

router = routers.DefaultRouter()
router.register(r'getposts', getmoto, basename='MotoSellViews')
router.register(r'users', views.users)

urlpatterns = [
    path('', include(router.urls)),

    #Posts
    path('postmoto/', postmoto.as_view({'post':'list'})),
    path('updateposts/<int:pk>', putmoto.as_view()),
    path('deleteposts/<int:pk>', deletemoto.as_view()),
    path('sortposts/', sort.as_view({'get':'list'})),

    #Users
    path('updateuser/<int:pk>', updateuser.as_view()),
    path('deleteuser/<int:pk>', deleteuser.as_view()),
    path('currentuser/', currentuser.as_view({'get':'list'})),

    #login
    path('login-rest/', Myobtain_auth_token.as_view()),
    #drf
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]