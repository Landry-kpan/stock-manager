from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = [
            "name",
            "category",
            "price",
            "quantity",
            "description",
        ]

        labels = {
            "name": "Nom du produit",
            "category": "Catégorie",
            "price": "Prix",
            "quantity": "Quantité",
            "description": "Description",
        }

        help_texts = {
            "name": "Entrez le nom du produit",
            "price": "Prix du produit",
            "quantity": "Quantité disponible en stock",
            "description": "Description du produit",
        }