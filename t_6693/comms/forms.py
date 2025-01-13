from django.forms import ModelForm  # type: ignore

from t_6693.comms.models import Comm  # type: ignore


class CommForm(ModelForm):
    class Meta:
        model = Comm
        fields = ("id", "max_descr", "min_descr_man", "min_descr_wom")
        labels = {
            "max_descr": "Описание",
            "min_descr_man": "Мужчина",
            "min_descr_wom": "Женщина",
        }
