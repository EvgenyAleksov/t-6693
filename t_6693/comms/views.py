from django.contrib.messages.views import SuccessMessageMixin  # type: ignore
from django.urls import reverse_lazy  # type: ignore
from django.views.generic import (  # type: ignore
    CreateView,
    ListView,
    UpdateView,
)

from t_6693.comms.forms import CommForm, CommUpdateForm  # type: ignore
from t_6693.comms.models import Comm  # type: ignore
from t_6693.mixins import ProjectLoginRequiredMixin  # type: ignore


class CommCreateView(
    SuccessMessageMixin, CreateView
):
    model = Comm
    form_class = CommForm
    template_name = "object.html"
    success_url = reverse_lazy("comm_list")
    success_message = "Запись успешно создана"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Создать ЧБО"
        context["button_text"] = "Создать"
        context["object"] = Comm.objects.count() + 1
        return context


class CommListView(ProjectLoginRequiredMixin, ListView):
    model = Comm
    template_name = "comms/comms.html"
    # context_object_name = "comms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "Comm"
        context["title"] = "Число Близкого Общения"
        context["rec_count"] = Comm.objects.count()
        context["rec_limit"] = 9
        context["result"] = Comm.objects.all
        return context


class CommUpdateView(
    ProjectLoginRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = Comm
    form_class = CommUpdateForm
    template_name = "object.html"
    success_url = reverse_lazy("comm_list")
    success_message = "Запись успешно изменена"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Изменить ЧБО"
        context["button_text"] = "Изменить"
        context["object"] = self.object.id
        return context
