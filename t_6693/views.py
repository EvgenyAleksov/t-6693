from django.contrib.auth.views import (  # type: ignore
    LoginView,
    LogoutView,
)
from django.contrib.messages.views import SuccessMessageMixin  # type: ignore
from django.urls import reverse_lazy  # type: ignore
from django.views.generic.base import TemplateView  # type: ignore

from .mixins import ProjectRedirectURLMixin


class IndexView(TemplateView):
    template_name = "index.html"


class LoginUser(SuccessMessageMixin, LoginView):
    template_name = "users/login.html"
    next_page = reverse_lazy("index")
    success_message = "Вы вошли в систему"


class LogoutUser(ProjectRedirectURLMixin, LogoutView):
    next_page = reverse_lazy("index")
    success_message = None
    info_message = "Вы вышли из системы"


class ConfirmView(ProjectRedirectURLMixin, TemplateView):
    template_name = "confirm.html"
