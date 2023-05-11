from django.urls import path
from rest_framework import routers

from shortener.urls.apis import UrlListView
from shortener.urls.views import url_list, url_create, url_change

router = routers.DefaultRouter()
router.register(r"urls", UrlListView)


urlpatterns = [
    path("", url_list, name="url_list"),
    path("create", url_create, name="url_create"),
    path("<str:action>/<int:url_id>", url_change, name="url_change"),
]
