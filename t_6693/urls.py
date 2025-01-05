from django.contrib import admin  # type: ignore
from django.urls import include, path  # type: ignore

from t_6693 import views  # type: ignore

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('калькулятор/', include('t_6693.calc.urls')),
    path('чбо/', include('t_6693.comms.urls')),
    path('миссия/', include('t_6693.missions.urls')),
    path('вдохновение/', include('t_6693.inspirations.urls')),
    path('совместимость-чбо/', include('t_6693.comps_comms.urls')),
    path('совместимость-миссия/', include('t_6693.comps_miss.urls')),

    path('пользователи/', include('t_6693.users.urls')),
    path('вход/', views.LoginUser.as_view(), name='login'),
    path('выход/', views.LogoutUser.as_view(), name='logout'),

    path("admin/", admin.site.urls),
]
