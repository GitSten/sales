from django.shortcuts import render
from django.db.models import Q
from .models import Product, Tag, News, ProductUpdate, Information


def product_list(request):
    search_query = request.GET.get('search', '')
    tag_filter = request.GET.get('tag', '')

    if search_query:
        products = Product.objects.filter(
            Q(name__icontains=search_query) |
            Q(code__icontains=search_query)
        )
    else:
        products = Product.objects.all()

    if tag_filter:
        products = products.filter(tags__name=tag_filter)

    # Lisa is_new atribuut iga toote jaoks
    for product in products:
        product.is_new = product.tags.filter(name="UUS").exists()

    tags = Tag.objects.all()
    news = News.objects.all()
    return render(request, 'index.html', {'products': products, 'search_query': search_query, 'tags': tags, 'news': news})

def new_products(request):
    products = ProductChange.objects.filter(change_type='new').order_by('-change_date')
    return render(request, 'new_products.html', {'products': products})

def product_changes(request):
    products = ProductChange.objects.filter(change_type='removed').order_by('-change_date')
    return render(request, 'product_changes.html', {'products': products})

def discontinued_products(request):
    product_updates = ProductUpdate.objects.all()
    return render(request, 'discontinued_products.html', {'product_updates': product_updates})



def info(request):
    info_entries = Information.objects.all()
    return render(request, 'info.html', {'info_entries': info_entries})