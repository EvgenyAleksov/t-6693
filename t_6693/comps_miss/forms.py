from django.forms import ModelForm  # type: ignore

from t_6693.comps_miss.models import Comp_Miss  # type: ignore


class Comp_MissForm(ModelForm):
    class Meta:
        model = Comp_Miss
        fields = ("name", "descr_1", "descr_2")
        labels = {
            "name": "Сочетание",
            "descr_1": "Описание Min",
            "descr_2": "Описание Max",
        }
