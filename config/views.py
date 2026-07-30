from django.shortcuts import render
from prducts.models import Product
from categories.models import Category
from stock.models import StockMovement


def home(request):
    products_count = Product.objects.count()
    categories_count = Category.objects.count()

    stock_total = sum(
        product.quantity
        for product in Product.objects.all()
    )

    low_stock_products = Product.objects.filter(
        quantity__gt=0,
        quantity__lte=5
    ).order_by("quantity")

    out_of_stock_products = Product.objects.filter(
        quantity=0
    ).order_by("name")

    recent_movements = StockMovement.objects.select_related(
        "product"
    ).order_by("-date")[:5]

    return render(
        request,
        "dashboard.html",
        {
            "products_count": products_count,
            "categories_count": categories_count,
            "stock_total": stock_total,
            "low_stock_products": low_stock_products,
            "out_of_stock_products": out_of_stock_products,
            "recent_movements": recent_movements,
        }
    )