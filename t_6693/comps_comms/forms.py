from django.forms import ModelForm  # type: ignore

from t_6693.comps_comms.models import Comp_Comm  # type: ignore


class Comp_CommForm(ModelForm):
    class Meta:
        model = Comp_Comm
        fields = ("name", "descr_1", "descr_2")
        labels = {
            "name": "Сочетание",
            "descr_1": "Описание Min",
            "descr_2": "Описание Max",
        }
