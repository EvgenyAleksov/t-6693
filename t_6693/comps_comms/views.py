from django.contrib.messages.views import SuccessMessageMixin  # type: ignore
from django.urls import reverse_lazy  # type: ignore
from django.views.generic import (  # type: ignore
    CreateView,
    ListView,
    UpdateView,
)

from t_6693.comps_comms.forms import Comp_CommForm  # type: ignore
from t_6693.comps_comms.models import Comp_Comm  # type: ignore
from t_6693.mixins import ProjectLoginRequiredMixin  # type: ignore


class Comp_CommListView(ProjectLoginRequiredMixin, ListView):
    model = Comp_Comm
    template_name = "comps_comms/comps_comms.html"
    # context_object_name = "comps_comms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "Comp_Comm"
        context["title"] = "Совместимость по ЧБО"
        context["rec_count"] = Comp_Comm.objects.count()
        context["rec_limit"] = 45
        context["result"] = Comp_Comm.objects.all
        return context


class Comp_CommCreateView(
    ProjectLoginRequiredMixin, SuccessMessageMixin, CreateView
):
    model = Comp_Comm
    form_class = Comp_CommForm
    template_name = "object.html"
    success_url = reverse_lazy("comp_comm_list")
    success_message = "Запись успешно создана"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Создать Совместимость по ЧБО"
        context["button_text"] = "Создать"
        return context


class Comp_CommUpdateView(
    ProjectLoginRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = Comp_Comm
    form_class = Comp_CommForm
    template_name = "object.html"
    success_url = reverse_lazy("comp_comm_list")
    success_message = "Запись успешно изменена"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Изменить Совместимость по ЧБО"
        context["button_text"] = "Изменить"
        context["object"] = self.object.name
        return context
