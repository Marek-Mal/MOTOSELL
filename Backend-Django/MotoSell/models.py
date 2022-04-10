from django.db import models
import datetime
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class myBaseUserManager(models.Manager):

    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the email address by lowercasing the domain part of it.
        """
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = email_name + '@' + domain_part.lower()
        return email

    def make_random_password(self, length=10,
                             allowed_chars='abcdefghjkmnpqrstuvwxyz'
                                           'ABCDEFGHJKLMNPQRSTUVWXYZ'
                                           '23456789'):
        """
        Generate a random password with the given length and given
        allowed_chars. The default value of allowed_chars does not have "I" or
        "O" or letters and digits that look similar -- just to avoid confusion.
        """
        return get_random_string(length, allowed_chars)

    def get_by_natural_key(self, email):
        return self.get(**{self.model.EMAIL_FIELD: email})

class MyUserManager(myBaseUserManager):
    def create_user(self, email, username, surname, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            surname=surname
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, surname, password):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            surname=surname
        )

        user.is_staff = False
        user.is_admin = False
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user
        

class MemberMotoSell(AbstractBaseUser):

    user_id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=100)
    surname = models.CharField(max_length=120)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255, default=".")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def has_module_perms(self, app_label):
        return True
    
    def has_perm(self, perm, obj=None):
        return True

    class Meta:
        #unique_fields = ('username',)
        app_label = "MotoSell"
        db_table = "_membermotosell"

class MotoSellModel(models.Model):

    category_choice = [
        ("motocykl", "motocykl"),
        ("osobowy", "osobowy"),
        ("ciężarowy", "ciężarowy"),
    ]

    fuel_choice = (
        ("benzyna", "benzyna"),
        ("disel", "disel"),
        ("LPG" ,"LPG"),
    )

    Moto_id = models.AutoField(primary_key=True, unique=True)
    price = models.PositiveBigIntegerField(default=100, blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    category = models.CharField(max_length=9, choices=category_choice, blank=False, null=False)
    mark = models.TextField(blank=False, null=False)
    model = models.TextField(blank=False, null=False)
    date_of_production = models.DateField(blank=False, null=False)
    course = models.PositiveBigIntegerField(blank=False, null=False)
    displacement = models.PositiveBigIntegerField(blank=False, null=False)
    power = models.PositiveBigIntegerField(blank=False, null=False)
    fuel = models.CharField(max_length=9, blank=False, null=False, choices=fuel_choice)
    photo = models.ImageField(null=True, blank=True)
    post_Moto = models.ForeignKey(MemberMotoSell, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
