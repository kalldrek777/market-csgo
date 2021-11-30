from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from weapons.models import Product
from weapons.forms import SearchForm


def home(request):
    qs = Product.objects.all().order_by('-date')
    paginator = Paginator(qs, 8)  # Show 8 contacts per page.
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form_query = form.cleaned_data
            #   print(form_query['query'])
            query = form_query['query']
            return render(request, 'Search.html', {'qs': qs, 'form': form, 'query': query})

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    dict = {'page_obj': page_obj, 'form': form}

    return render(request, 'home.html', dict)



