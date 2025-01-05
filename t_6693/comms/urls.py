from django.urls import path  # type: ignore

from t_6693.comms.views import (  # type: ignore
    CommCreateView,
    CommListView,
    CommUpdateView,
)

urlpatterns = [
    path("", CommListView.as_view(), name="comm_list"),
    path("создать/", CommCreateView.as_view(), name="comm_create"),
    path("<int:pk>/изменить/", CommUpdateView.as_view(), name="comm_update"),
]
