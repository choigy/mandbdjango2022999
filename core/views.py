from django.shortcuts import render
from movies.models import Movie
from books.models import Book
from people.models import Person
from categories.models import Category

def resolve_home(request):
  

  movies = Movie.objects.all().order_by('-pk')[:9]
  books = Book.objects.all().order_by('-pk')[:9]
  people = Person.objects.all().order_by('-pk')[:9]
  

  return render(request, "home.html", {
    "movies":movies,
    "books": books,
    "people": people,
    "page_title": "Home"
  })



def resolve_search(request):
  capi=request.GET.get('name')
  if capi:
    name=capi.capitalize()
    people=Person.objects.filter(name__startswith=name)
    movies=Movie.objects.filter(title__startswith=name)
    books=Book.objects.filter(title__startswith=name)
    print(people, movies, books)
    return render(request, "search.html", {
      'people':people, 'movies':movies, 'books':books, 
    })
  return render(request, "search.html", {
    'categories':Category.objects.all()
    })