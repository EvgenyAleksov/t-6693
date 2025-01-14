from datetime import datetime  # type: ignore

from django import forms  # type: ignore


class CalcForm_1(forms.Form):

    sex = forms.IntegerField(
        widget=forms.RadioSelect(
            attrs={'display': 'inline-block'},
            choices=((1, "Мужчина"), (2, "Женщина")),
        ),
        label=""
    )

    name = forms.CharField(
        max_length=25, required=False, label="Имя", help_text="(по желанию)"
    )

    birthday = forms.DateField(
        input_formats=["%d.%m.%Y"],
        widget=forms.DateInput(
            attrs={
                type: "date",
                "data-mask": "00.00.0000",
            }
        ),
        required=True,
        label="Дата рождения",
        error_messages={"invalid": "Введите корректную дату"},
    )

    def clean_birthday(self):
        return val_bd(self.cleaned_data.get("birthday"))


class CalcForm_2(forms.Form):
    name_1 = forms.CharField(
        max_length=25,
        required=False,
        label="Имя 1",
        help_text="(по желанию)",
    )
    birthday_1 = forms.DateField(
        input_formats=["%d.%m.%Y"],
        widget=forms.DateInput(
            attrs={
                type: "date",
                "data-mask": "00.00.0000",
            }
        ),
        required=True,
        label="Дата рождения 1",
        error_messages={"invalid": "Введите корректную дату"},
    )
    name_2 = forms.CharField(
        max_length=25,
        required=False,
        label="Имя 2",
        help_text="(по желанию)",
    )
    birthday_2 = forms.DateField(
        input_formats=["%d.%m.%Y"],
        widget=forms.DateInput(
            attrs={
                type: "date",
                "data-mask": "00.00.0000",
            }
        ),
        required=True,
        label="Дата рождения 2",
        error_messages={"invalid": "Введите корректную дату"},
    )

    def clean_birthday_1(self):
        return val_bd(self.cleaned_data.get("birthday_1"))

    def clean_birthday_2(self):
        return val_bd(self.cleaned_data.get("birthday_2"))


def val_bd(bd):
    bd1 = bd.strftime("%d.%m.%Y")
    year = datetime.strptime(bd1, "%d.%m.%Y").year
    if year not in range(1900, 2101):
        raise forms.ValidationError("Допустимое значение года от 1900 до 2100")
    return bd
