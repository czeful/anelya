from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request):
    context = {"title": "Home - Главная", "content": "Магазин мебели HOME"}
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Пизда какой ахуенный магаз, покупайте суки, мебель",
    }
    return render(request, "main/about.html", context)
