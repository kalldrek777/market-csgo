from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from weapons.models import Product
from weapons.forms import SearchForm


def home(request):
    qs = Product.objects.all().order_by('-date')
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
            for i in qs:
                if query in i.name:
                    a.append(i)
                    paginator = Paginator(a, 8)  # Show 8 contacts per page.

                    page_number = request.GET.get('page')
                    page_obj = paginator.get_page(page_number)
            return render(request, 'Search.html', {'page_obj': page_obj, 'form': form, 'query': query})

    dict = {'page_obj': page_obj, 'form': form}

    return render(request, 'home.html', dict)






