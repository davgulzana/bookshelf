from django.views.generic import ListView, DetailView

from main.models import Book


class BooksListView(ListView):
    paginate_by = 2
    model = Book
    template_name = 'main/index.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'main/detail.html'