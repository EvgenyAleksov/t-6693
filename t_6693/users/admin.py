from django.contrib import admin  # type: ignore
from django.contrib.auth.admin import UserAdmin  # type: ignore

from t_6693.users.forms import UserForm, UserUpdateForm  # type: ignore
from t_6693.users.models import CustomUser  # type: ignore


class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form = UserUpdateForm
    model = CustomUser
    list_display = ['id', 'username', 'email']


admin.site.register(CustomUser, CustomUserAdmin)

