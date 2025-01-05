from django.contrib.auth.forms import (  # type: ignore
    UserChangeForm,
    UserCreationForm,
)
from django.forms import CharField  # type: ignore

from t_6693.users.models import CustomUser  # type: ignore


class UserForm(UserCreationForm):
    username = CharField(
        max_length=22,
        label="Имя")

    email = CharField(
        max_length=30,
        required=True,
        label="e-mail")

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class UserUpdateForm(UserChangeForm):
    username = CharField(
        max_length=22,
        label="Имя")

    email = CharField(
        max_length=30,
        required=True,
        label="e-mail")

    password = None

    password1 = CharField(
        label="Пароль",
        strip=False,
        )

    password2 = CharField(
        label="Подтверждение пароля",
        strip=False,
        help_text="Введите пароль ешё раз"
        )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
