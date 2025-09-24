from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):
    return render(request, "don_julio_pub/index.html")


def show_contacts(request: HttpRequest):
    return render(request, "don_julio_pub/contacts.html")
