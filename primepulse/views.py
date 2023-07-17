from django.shortcuts import render
from store.models import Product
from django.contrib.sitemaps import Sitemap
from django.urls import reverse


def home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }
    return render(request, 'index.html', context)


def page_not_found(request, slug):
    return render(request, '404.html', status=404)


class MySitemap(Sitemap):
    def items(self):
        return ['home', 'products', 'about', 'contact']

    def location(self, item):
        return reverse(item)

sitemaps = {
    'site': MySitemap,
}