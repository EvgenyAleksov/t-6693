from django.contrib.messages.views import SuccessMessageMixin  # type: ignore
from django.urls import reverse_lazy  # type: ignore
from django.views.generic import (  # type: ignore
    CreateView,
    ListView,
    UpdateView,
)

from t_6693.inspirations.forms import InspirationForm  # type: ignore
from t_6693.inspirations.models import Inspiration  # type: ignore
from t_6693.mixins import ProjectLoginRequiredMixin  # type: ignore


class InspirationListView(ProjectLoginRequiredMixin, ListView):
    model = Inspiration
    template_name = "inspirations/inspirations.html"
    # context_object_name = "inspirations"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "Inspiration"
        context["title"] = "Вдохновение"
        context["rec_count"] = Inspiration.objects.count()
        context["rec_limit"] = 22
        context["result"] = Inspiration.objects.all
        return context


class InspirationCreateView(
    ProjectLoginRequiredMixin, SuccessMessageMixin, CreateView
):
    model = Inspiration
    form_class = InspirationForm
    template_name = "object.html"
    success_url = reverse_lazy("inspiration_list")
    success_message = "Запись успешно создана"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Создать Вдохновение"
        context["button_text"] = "Создать"
        context["object"] = Inspiration.objects.count() + 1
        return context
 

class InspirationUpdateView(
    ProjectLoginRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = Inspiration
    form_class = InspirationForm
    template_name = "object.html"
    success_url = reverse_lazy("inspiration_list")
    success_message = "Запись успешно изменена"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Изменить Вдохновение"
        context["button_text"] = "Изменить"
        context["object"] = self.object.id
        return context
    