from django.forms import ModelForm  # type: ignore

from t_6693.comms.models import Comm  # type: ignore


class CommForm(ModelForm):
    class Meta:
        model = Comm
        fields = ("id", "descr")
        labels = {"descr": "Описание"}


class CommUpdateForm(ModelForm):
    class Meta:
        model = Comm
        fields = ["descr"]
        labels = {"descr": "Описание"}
