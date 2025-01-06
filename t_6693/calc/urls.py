from django.urls import path  # type: ignore

from t_6693.calc.views import (  # type: ignore
    Calc_1_PDF_View,
    Calc_1_View,
    Calc_2_PDF_View,
    Calc_2_View,
)

descr = "PВF"

urlpatterns = [
    path("1", Calc_1_View.as_view(), name="calc_1"),
    path("2", Calc_2_View.as_view(), name="calc_2"),
    path(
        f"Описание {descr}",
        Calc_1_PDF_View.as_view(),
        name="calc_1_pdf",
    ),
    path("pdf-2", Calc_2_PDF_View.as_view(), name="calc_2_pdf"),
]
