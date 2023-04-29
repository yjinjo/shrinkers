from django.db.models import F

from shortener.models import Users


def url_count_changer(request, is_increase: bool):
    count_number = 1 if is_increase else -1
    Users.objects.filter(user_id=request.user.id).update(
        url_count=F("url_count") + count_number
    )
