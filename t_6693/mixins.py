from django.contrib import messages  # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin  # type: ignore
from django.contrib.auth.views import RedirectURLMixin  # type: ignore
from django.shortcuts import redirect  # type: ignore
from django.urls import reverse_lazy  # type: ignore


class ProjectLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy("login")
    denied_message = "Для доступа нужно войти в систему"

    def handle_no_permission(self):
        messages.error(self.request, self.denied_message)
        return redirect(self.login_url)


class ProjectRedirectURLMixin(RedirectURLMixin):

    def get_default_redirect_url(self):
        if self.next_page:
            if self.success_message:
                messages.success(self.request, self.success_message)
            elif self.info_message:
                messages.info(self.request, self.info_message)
        return super().get_default_redirect_url()
