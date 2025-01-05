from django.urls import path  # type: ignore

from t_6693.comps_comms.views import (  # type: ignore
    Comp_CommCreateView,
    Comp_CommListView,
    Comp_CommUpdateView,
)

urlpatterns = [
    path("", Comp_CommListView.as_view(), name="comp_comm_list"),
    path("создать/", Comp_CommCreateView.as_view(), name="comp_comm_create"),
    path(
        "<int:pk>/изменить/",
        Comp_CommUpdateView.as_view(),
        name="comp_comm_update",
    ),
]
