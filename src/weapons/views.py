from django.core.paginator import Paginator
from django.shortcuts import render
from weapons.models import Product
from weapons.forms import SearchForm

__all__ = (
    'weapons',
    'knife',
)


def knife(request):
    qs = Product.objects.all().order_by('-date').filter(category='Ножи')
    paginator = Paginator(qs, 8)  # Show 8 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form_query = form.cleaned_data
            #   print(form_query['query'])
            query = form_query['query']
            a = []
            qs = Product.objects.all().order_by('-date')
            for i in qs:
                if query in i.name:
                    a.append(i)
                    paginator = Paginator(a, 8)  # Show 8 contacts per page.

                    page_number = request.GET.get('page')
                    page_obj = paginator.get_page(page_number)
            return render(request, 'Search.html', {'page_obj': page_obj, 'form': form, 'query': query})

    dict = {'page_obj': page_obj, 'form': form}

    return render(request, 'weapons/knifes.html', dict)


def weapons(request):
    qs = Product.objects.all().order_by('-date').filter(category='Оружия')
    paginator = Paginator(qs, 8)  # Show 8 contacts per page.

    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form_query = form.cleaned_data
            #   print(form_query['query'])
            query = form_query['query']
            a = []
            qs = Product.objects.all().order_by('-date')
            for i in qs:
                if query in i.name:
                    a.append(i)
                    paginator = Paginator(a, 8)  # Show 8 contacts per page.

                    page_number = request.GET.get('page')
                    page_obj = paginator.get_page(page_number)
            return render(request, 'Search.html', {'page_obj': page_obj, 'form': form, 'query': query})

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    dict = {'page_obj': page_obj, 'form': form}

    return render(request, 'weapons/weapons.html', dict)








