from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')

    result = Phone.objects.all()

    if sort == 'min_price':
        result = sorted(result, key=lambda x: x.price)
    elif sort == 'max_price':
        result = sorted(result, key=lambda x: x.price, reverse=True)
    elif sort == 'name':
        result = sorted(result, key=lambda x: x.name)

    context = {
        'phones': result
    }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    context = {
        'phone': Phone.objects.filter(slug=slug).first()
    }

    return render(request, template, context)
