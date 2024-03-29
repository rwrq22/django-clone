from django.urls import path
from . import views

urlpatterns = [
    path("", views.Categories.as_view()),
    path("<int:pk>", views.CategoryDetail.as_view()),
]

# ModelViewSet Version
""" urlpatterns = [
    path(
        "",
        views.CategoryViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            },
        ),
    ),
    path(
        "<int:pk>",
        views.CategoryViewSet.as_view(
            {
                "get": "retrieve",  # Select an obj
                "put": "partial_update",
                "delete": "destroy",
            },
        ),
    ),
] """
