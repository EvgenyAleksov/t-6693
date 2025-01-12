from django.contrib import admin  # type: ignore
from django.contrib.auth.admin import UserAdmin  # type: ignore

from t_6693.users.forms import UserForm, UserUpdateForm  # type: ignore
from t_6693.users.models import User  # type: ignore


class UserAdmin(UserAdmin):
    add_form = UserForm
    form = UserUpdateForm
    model = User
    list_display = ['username', 'email']


admin.site.register(User, UserAdmin)
