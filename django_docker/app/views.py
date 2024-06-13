from django.shortcuts import render
from django.views import View
from .models import Product


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "product.html", context={"products": products})
