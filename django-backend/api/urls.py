from django.urls import path
from .views import signup, login_view, me, get_profile, update_profile, logout_view

urlpatterns = [
    path("signup/", signup),
    path("login/", login_view),
    path("me/", me),
    path("profile/", get_profile),
    path("profile/update/", update_profile),
    path("profile/logout/", logout_view)
]