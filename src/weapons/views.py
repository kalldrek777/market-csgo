from django.core.paginator import Paginator
from django.shortcuts import render
from weapons.models import Product
from weapons.forms import SearchForm

__all__ = (
    'weapons',
    'knife',
)


def knife(request):
    qs = Product.objects.all().order_by('-date')
    paginator = Paginator(qs, 8)  # Show 8 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    dict = {'page_obj': page_obj}

    return render(request, 'weapons/knifes.html', dict)


def weapons(request):
    qs = Product.objects.all().order_by('-date')
    paginator = Paginator(qs, 8)  # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    dict = {'page_obj': page_obj}
    return render(request, 'weapons/weapons.html', dict)








