from django.contrib.auth.forms import PasswordChangeForm  # type: ignore
from django.contrib.auth.views import PasswordChangeView  # type: ignore
from django.contrib.messages.views import SuccessMessageMixin  # type: ignore
from django.urls import reverse_lazy  # type: ignore
from django.views.generic import (  # type: ignore
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from t_6693.mixins import (  # type: ignore
    # HasPermissionUserChangeMixin,
    ProjectLoginRequiredMixin,
)
from t_6693.users.forms import (  # type: ignore
    UserForm,
    UserUpdateForm,
)
from t_6693.users.models import CustomUser  # type: ignore


class UserCreateView(
    ProjectLoginRequiredMixin, SuccessMessageMixin, CreateView
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


class UserListView(ProjectLoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "users/users.html"
    # context_object_name = "users"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "User"
        context["title"] = "Пользователи"
        context["rec_count"] = CustomUser.objects.count()
        context["rec_limit"] = 3
        context["result"] = CustomUser.objects.exclude(id=1)
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


class PasswordUpdateView(
    ProjectLoginRequiredMixin, SuccessMessageMixin, PasswordChangeView
):
    model = CustomUser
    form_class = PasswordChangeForm
    template_name = "object.html"
    success_url = reverse_lazy("user_list")
    success_message = "Пароль успешно изменён"
    extra_context = {"title": "Изменить пароль", "button_text": "Изменить"}


class UserDeleteView(
    ProjectLoginRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = CustomUser
    template_name = "users/user_delete.html"
    success_url = reverse_lazy("user_list")
    success_message = "Пользователь успешно удалён"
    denied_url = reverse_lazy("user_list")
    # permission_denied_message = "Вы можете удалять только свою запись"

    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context["name"] = user.username
        return context
