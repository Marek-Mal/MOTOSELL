from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import MotoSellModel, MemberMotoSell, myBaseUserManager
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.views import obtain_auth_token, ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import serializers

UserModel = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MemberMotoSell
        fields = ('user_id', 'username', 'surname', 'email', 'password')
        extra_kwargs = {'password': {'write_only':True, 'required': True}}

    def create(self, validated_data):
        user = MemberMotoSell.objects.create_user(validated_data['email'], validated_data['username'], validated_data['surname'], validated_data['password'])
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.surname = validated_data['surname']
        instance.email = validated_data['email']

        instance.save()

        return instance

class MotoSellSerializer(serializers.ModelSerializer):

    user = UserSerializer(source='post_Moto', read_only=True)

    class Meta:
        model = MotoSellModel
        fields = ('Moto_id','title','price','description','category','mark','model','date_of_production','course','displacement','power','fuel','photo','post_Moto','user')



def user_can_authenticate(user):
        """
        Reject users with is_active=False. Custom user models that don't have
        that attribute are allowed.
        """
        is_active = getattr(user, 'is_active', None)
        return is_active or is_active is None

def authenticate(request, email=None, password=None, **kwargs):
        if email is None:
            email = kwargs.get(UserModel.EMAIL_FIELD)
        if email is None or password is None:
            return
        try:
            user = MemberMotoSell.objects.get_by_natural_key(email)
        except Exception as e:
            print(str(e))
            print('='*30)
            print('error')
            print('='*30)
        else:
            if user.check_password(password) and user_can_authenticate(user):
                return user

class MyAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "Email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

