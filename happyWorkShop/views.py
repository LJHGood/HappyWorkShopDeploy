from django.shortcuts import render  # , redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from happyWorkShop.models import *

# Create your views here.


def index(request):
    return render(request, "index.html")


def contactUsView(request):
    _name = request.POST["name_value"]
    _email = request.POST["email_value"]
    _phone = request.POST["phone_value"]
    _content = request.POST["content_value"]

    contactUsView = ContactUsModel(
        name=_name, email=_email, phone=_phone, content=_content)
    contactUsView.save()

    return HttpResponseRedirect(reverse("index"))
    # return redirect("index")
