

# Create your models here.
from django.db import models
from prducts.models import Product


class StockMovement(models.Model):

    MOVEMENT_TYPES = [
        ("IN", "Entrée"),
        ("OUT", "Sortie"),
    ]


    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    movement_type = models.CharField(
        max_length=3,
        choices=MOVEMENT_TYPES
    )

    quantity = models.PositiveIntegerField()

    date = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{self.product.name} - {self.movement_type}"