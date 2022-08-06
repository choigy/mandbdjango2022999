from django.shortcuts import render
from .models import Category
from books.models import Book
from movies.models import Movie

def resolve_categories(request, pk):
  category=Category.objects.get(pk=pk)
  books=category.books.all()
  movies=category.movies.all()
  print(books,movies)
  return render(request, "genres.html", {'books':books, 'movies':movies})