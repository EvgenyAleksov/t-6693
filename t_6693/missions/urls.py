from django.urls import path  # type: ignore

from t_6693.missions.views import (  # type: ignore
    MissionCreateView,
    MissionListView,
    MissionUpdateView,
)

urlpatterns = [
    path("", MissionListView.as_view(), name="mission_list"),
    path("создать/", MissionCreateView.as_view(), name="mission_create"),
    path(
        "<int:pk>/изменить/", MissionUpdateView.as_view(), name="mission_update"
    ),
]
