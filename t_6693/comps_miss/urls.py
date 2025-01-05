from django.urls import path  # type: ignore

from t_6693.comps_miss.views import (  # type: ignore
    Comp_MissCreateView,
    Comp_MissListView,
    Comp_MissUpdateView,
)

urlpatterns = [
    path("", Comp_MissListView.as_view(), name="comp_miss_list"),
    path("создать/", Comp_MissCreateView.as_view(), name="comp_miss_create"),
    path(
        "<int:pk>/изменить/",
        Comp_MissUpdateView.as_view(),
        name="comp_miss_update",
    ),
]
