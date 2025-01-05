from django.contrib.messages.views import SuccessMessageMixin  # type: ignore
from django.urls import reverse_lazy  # type: ignore
from django.views.generic import (  # type: ignore
    CreateView,
    ListView,
    UpdateView,
)

from t_6693.comps_miss.forms import Comp_MissForm  # type: ignore
from t_6693.comps_miss.models import Comp_Miss  # type: ignore
from t_6693.mixins import ProjectLoginRequiredMixin  # type: ignore


class Comp_MissListView(ProjectLoginRequiredMixin, ListView):
    model = Comp_Miss
    template_name = "comps_miss/comps_miss.html"
    # context_object_name = "comps_miss"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "Comp_Miss"
        context["title"] = "Совместимость по Миссии"
        context["rec_count"] = Comp_Miss.objects.count()
        context["rec_limit"] = 45
        context["result"] = Comp_Miss.objects.all
        return context


class Comp_MissCreateView(
    ProjectLoginRequiredMixin, SuccessMessageMixin, CreateView
):
    model = Comp_Miss
    form_class = Comp_MissForm
    template_name = "object.html"
    success_url = reverse_lazy("comp_miss_list")
    success_message = "Запись успешно создана"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Создать Совместимость по Миссии"
        context["button_text"] = "Создать"
        return context


class Comp_MissUpdateView(
    ProjectLoginRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = Comp_Miss
    form_class = Comp_MissForm
    template_name = "object.html"
    success_url = reverse_lazy("comp_miss_list")
    success_message = "Запись успешно изменена"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Изменить Совместимость по Миссии"
        context["button_text"] = "Изменить"
        context["object"] = self.object.name
        return context
