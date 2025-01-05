from django.urls import path  # type: ignore

from t_6693.inspirations.views import (  # type: ignore
    InspirationCreateView,
    InspirationListView,
    InspirationUpdateView,
)

urlpatterns = [
    path("", InspirationListView.as_view(), name="inspiration_list"),
    path(
        "создать/",
        InspirationCreateView.as_view(),
        name="inspiration_create"
    ),
    path(
        "<int:pk>/изменить/",
        InspirationUpdateView.as_view(),
        name="inspiration_update",
    ),
]
