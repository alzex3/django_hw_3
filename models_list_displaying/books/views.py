from django.shortcuts import render, redirect
from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'

    context = {
        'books': Book.objects.all()
    }

    return render(request, template, context)


def books_date(request, date):
    template = 'books/books_list.html'
    books_all = Book.objects.all()
    books_on_date = books_all.filter(pub_date=date)

    prev_date = ''
    next_date = ''
    if books_on_date:
        chosen_date = books_on_date.first().pub_date

        prev_date = books_all.filter(pub_date__lt=chosen_date).order_by('-pub_date').first()
        if prev_date:
            prev_date = str(prev_date.pub_date)

        next_date = books_all.filter(pub_date__gt=chosen_date).order_by('pub_date').first()
        if next_date:
            next_date = str(next_date.pub_date)

    context = {
        'books': books_on_date,
        'prev': prev_date,
        'next': next_date
    }

    return render(request, template, context)
