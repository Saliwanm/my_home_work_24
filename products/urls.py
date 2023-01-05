from django.urls import path
from . import views

urlpatterns = [
    path("/add", views.add_product, name="add_product"),
    path("/edit/<int:id>", views.edit_product, name="edit_product"),
    path("/update/<int:id>", views.update_product, name="update_product"),
    path("/<int:pk>/delete", views.ProductDeleteView.as_view(), name='delete_product'),
    path("/category", views.all_category, name="all_category"),
    path("/category/add", views.add_category, name="add_category"),
    path('/category/edit/<int:id>', views.edit_category, name="edit_category"),
    path("/category/update/<int:id>", views.update_category, name="update_category"),
    path("/<int:id>", views.product_details, name="product_details"),
]