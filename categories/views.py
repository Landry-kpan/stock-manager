from django.shortcuts import render, redirect, get_object_or_404      

# Create your views here.

from .models import Category
from .forms import CategoryForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, "categories/category_list.html", {
        "categories": categories
    })

def category_create(request):
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("category_list")

    return render(request, "categories/category_form.html", {
        "form": form
    })

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)

    form = CategoryForm(request.POST or None, instance=category)

    if form.is_valid():
        form.save()
        return redirect("category_list")

    return render(request, "categories/category_form.html", {
        "form": form
    })

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        category.delete()
        return redirect("category_list")

    return render(request, "categories/category_confirm_delete.html", {
        "category": category
    })