from django.urls import path  # type: ignore

from t_6693.users.views import (  # type: ignore
    PasswordUpdateView,
    UserCreateView,
    UserListView,
    UserUpdateView,
)

urlpatterns = [
    path("", UserListView.as_view(), name="user_list"),
    path("создать/", UserCreateView.as_view(), name="user_create"),
    path("<int:pk>/изменить", UserUpdateView.as_view(), name="user_update"),
    path(
        "сменить-пароль", PasswordUpdateView.as_view(), name="password_update"
    ),
]
