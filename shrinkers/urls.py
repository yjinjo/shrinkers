from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from shortener.views import index, get_user

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("get_user/<int:user_id>", get_user),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),  # Django Debug Toolbar
    ]
