from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Product
from .forms import ProductForm


def product_list(request):

    search = request.GET.get("search", "").strip()

    products = Product.objects.all()

    if search:
        products = products.filter(
            Q(name__icontains=search) |
            Q(category__name__icontains=search)
        )

    return render(
        request,
        "prducts/product_list.html",
        {
            "products": products,
            "search": search,
        }
    )


def product_create(request):

    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("product_list")

    return render(
        request,
        "prducts/product_form.html",
        {
            "form": form
        }
    )


def product_update(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    form = ProductForm(
        request.POST or None,
        instance=product
    )

    if form.is_valid():
        form.save()
        return redirect("product_list")

    return render(
        request,
        "prducts/product_form.html",
        {
            "form": form
        }
    )


def product_delete(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    if request.method == "POST":
        product.delete()
        return redirect("product_list")

    return render(
        request,
        "prducts/product_confirm_delete.html",
        {
            "product": product
        }
    )