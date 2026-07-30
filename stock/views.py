from django.shortcuts import render, redirect
from django.contrib import messages

from .models import StockMovement
from .forms import StockMovementForm


def movement_list(request):

    movements = StockMovement.objects.select_related(
        "product"
    ).order_by("-date")

    return render(
        request,
        "stock/movement_list.html",
        {
            "movements": movements
        }
    )


def movement_create(request):

    form = StockMovementForm(request.POST or None)

    if form.is_valid():

        movement = form.save(commit=False)

        product = movement.product

        # =========================
        # SORTIE DE STOCK
        # =========================

        if movement.movement_type == "OUT":

            if movement.quantity > product.quantity:

                messages.error(
                    request,
                    "Stock insuffisant pour ce produit."
                )

                return render(
                    request,
                    "stock/movement_form.html",
                    {
                        "form": form
                    }
                )

            product.quantity -= movement.quantity

        # =========================
        # ENTRÉE DE STOCK
        # =========================

        else:

            product.quantity += movement.quantity

        # Enregistrer la nouvelle quantité
        product.save()

        # Enregistrer le mouvement
        movement.save()

        messages.success(
            request,
            "Mouvement enregistré avec succès."
        )

        return redirect("movement_list")

    return render(
        request,
        "stock/movement_form.html",
        {
            "form": form
        }
    )