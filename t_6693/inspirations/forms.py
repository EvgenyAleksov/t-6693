from django.forms import ModelForm  # type: ignore

from t_6693.inspirations.models import Inspiration  # type: ignore


class InspirationForm(ModelForm):
    class Meta:
        model = Inspiration
        fields = ("id", "descr")
        labels = {"descr": "Описание"}


class CommUpdateForm(ModelForm):
    class Meta:
        model = Inspiration
        fields = ["descr"]
        labels = {"descr": "Описание"}
