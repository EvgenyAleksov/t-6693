from django.contrib.auth.forms import PasswordChangeForm  # type: ignore
from django.contrib.auth.views import PasswordChangeView  # type: ignore
from django.contrib.messages.views import SuccessMessageMixin  # type: ignore
from django.urls import reverse_lazy  # type: ignore
from django.views.generic import (  # type: ignore
    CreateView,
    ListView,
    UpdateView,
)

from t_6693.mixins import ProjectLoginRequiredMixin  # type: ignore
from t_6693.users.forms import (  # type: ignore
    UserForm,
    UserUpdateForm,
)
from t_6693.users.models import CustomUser  # type: ignore


class PasswordUpdateView(
    ProjectLoginRequiredMixin, SuccessMessageMixin, PasswordChangeView
):
    model = CustomUser
    form_class = PasswordChangeForm
    template_name = "object.html"
    success_url = reverse_lazy("user_list")
    success_message = "Пароль успешно сменён"
    extra_context = {"title": "Сменить пароль", "button_text": "Сменить"}


class UserListView(ProjectLoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "users/users.html"
    # context_object_name = "users"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "CustomUser"
        context["title"] = "Пользователи"
        context["rec_count"] = CustomUser.objects.count()
        context["rec_limit"] = 2
        context["result"] = CustomUser.objects.all
        return context


class UserCreateView(
    SuccessMessageMixin, CreateView
):
    model = CustomUser
    form_class = UserForm
    template_name = "object.html"
    success_url = reverse_lazy("user_list")
    success_message = "Запись успешно создана"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Создать Пользователя"
        context["button_text"] = "Создать"
        context["object"] = CustomUser.objects.count() + 1
        return context


class UserUpdateView(
    ProjectLoginRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = CustomUser
    form_class = UserUpdateForm
    template_name = "object.html"
    success_url = reverse_lazy("user_list")
    success_message = "Запись успешно изменена"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Изменить Пользователя"
        context["button_text"] = "Изменить"
        context["object"] = self.object.id
        return context
