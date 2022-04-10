from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import MemberMotoSell, MotoSellModel

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MemberMotoSell
        fields = ('email', 'username','surname', 'password', 'is_active', 'is_admin', 'is_staff')


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email','username','surname', 'password', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email','username','surname', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_staff',)}),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(MemberMotoSell, UserAdmin)
admin.site.register(MotoSellModel)