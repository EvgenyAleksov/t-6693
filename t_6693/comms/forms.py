from django.forms import ModelForm  # type: ignore

from t_6693.comms.models import Comm  # type: ignore


class CommForm(ModelForm):
    class Meta:
        model = Comm
        fields = ("id", "descr", "descr_man", "descr_wom")
        labels = {
            "descr": "Описание",
            "descr_man": "Мужчина",
            "descr_wom": "Женщина",
        }


class CommUpdateForm(ModelForm):
    class Meta:
        model = Comm
        fields = ["descr", "descr_man", "descr_wom"]
        labels = {
            "descr": "Описание",
            "descr_man": "Мужчина",
            "descr_wom": "Женщина",
        }
