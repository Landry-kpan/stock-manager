from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.movement_list,
        name="movement_list"
    ),

    path(
        "add/",
        views.movement_create,
        name="movement_create"
    ),

]