from django.shortcuts import render

from rest_framework.views import APIView


def home(request):
    return render(request, "home.html")
