from django.forms import ModelForm  # type: ignore

from t_6693.missions.models import Mission  # type: ignore


class MissionForm(ModelForm):
    class Meta:
        model = Mission
        fields = ("id", "descr")
        labels = {"descr": "Описание"}


class MissionUpdateForm(ModelForm):
    class Meta:
        model = Mission
        fields = ["descr"]
        labels = {"descr": "Описание"}
