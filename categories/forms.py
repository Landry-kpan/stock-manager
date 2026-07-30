from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category

        fields = [
            "name",
        ]

        labels = {
            "name": "Nom de la catégorie",
        }

        help_texts = {
            "name": "Entrez le nom de la catégorie",
        }