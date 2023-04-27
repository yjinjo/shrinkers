from django.shortcuts import render, redirect

from shortener.models import Users


# Create your views here.
def index(request):
    user = Users.objects.filter(username="admin").first()
    email = user.email if user else "Anonymous User!"

    return render(request, "base.html", {"welcome_msg": f"Hello {email}"})


def redirect_test(request):
    print("Go Redirect")
    return redirect("index")
