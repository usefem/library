from django.urls import path

from .views import BookListView, BookDetailView


urlpatterns = [
    path("", BookListView.as_view(), name="home"),
    path('<pk>/', BookDetailView.as_view()),
]
