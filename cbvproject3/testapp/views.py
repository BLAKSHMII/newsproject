from django.shortcuts import render
from django.views.generic import ListView
from testapp.models import Book
# Create your views here.
class BookListView(ListView):
    model=Book
