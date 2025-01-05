from django.contrib.messages.views import SuccessMessageMixin  # type: ignore
from django.urls import reverse_lazy  # type: ignore
from django.views.generic import (  # type: ignore
    CreateView,
    ListView,
    UpdateView,
)

from t_6693.missions.forms import MissionForm, MissionUpdateForm  # type: ignore
from t_6693.missions.models import Mission  # type: ignore
from t_6693.mixins import ProjectLoginRequiredMixin  # type: ignore


class MissionListView(ProjectLoginRequiredMixin, ListView):
    model = Mission
    template_name = "missions/missions.html"
    # context_object_name = "missions"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "Mission"
        context["title"] = "Миссия"
        context["rec_count"] = Mission.objects.count()
        context["rec_limit"] = 9
        context["result"] = Mission.objects.all
        return context


class MissionCreateView(
    ProjectLoginRequiredMixin, SuccessMessageMixin, CreateView
):
    model = Mission
    form_class = MissionForm
    template_name = "object.html"
    success_url = reverse_lazy("mission_list")
    success_message = "Запись успешно создана"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Создать Миссию"
        context["button_text"] = "Создать"
        context["object"] = Mission.objects.count() + 1
        context["ur"] = "url 'mission_create'"
        return context


class MissionUpdateView(
    ProjectLoginRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = Mission
    form_class = MissionUpdateForm
    template_name = "object.html"
    success_url = reverse_lazy("mission_list")
    success_message = "Запись успешно изменена"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Изменить Миссию"
        context["button_text"] = "Изменить"
        context["object"] = self.object.id
        return context
