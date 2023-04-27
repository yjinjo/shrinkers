from django.contrib import admin
from django.urls import path

from shortener.views import index, get_user

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("get_user/<int:user_id>", get_user),
]
