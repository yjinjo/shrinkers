from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from shortener.urls.urls import router as url_router
from shortener.urls.views import url_redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shortener.index.urls")),
    path("urls/", include("shortener.urls.urls")),
    path("api/", include(url_router.urls)),
    path("<str:prefix>/<str:url>", url_redirect),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),  # Django Debug Toolbar
    ]
