from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("quiz", views.quiz, name="quiz"),
    path("quiz/results", views.results, name="results"),
    path("categories", views.categories, name="categories"),
    path("categories/<int:id>", views.category, name="category"),
]