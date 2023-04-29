from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from shortener.views import (
    index,
    get_user,
    register,
    login_view,
    logout_view,
    list_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("register", register, name="register"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("list", list_view, name="list_view"),
    path("get_user/<int:user_id>", get_user),
    path("urls/", include("shortener.urls.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),  # Django Debug Toolbar
    ]
