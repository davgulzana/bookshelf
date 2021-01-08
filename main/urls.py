from django.urls import path

from main.views import BooksListView, BookDetailView

urlpatterns = [
    path('', BooksListView.as_view(), name='home-page'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='detail'),
]
