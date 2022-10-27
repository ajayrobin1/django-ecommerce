from django.urls import path

from . import views

app_name = "product"

urlpatterns = [
    path("", views.HomePage.as_view(), name="index"),
    path("sell/", views.CreateProduct.as_view(), name="sell"),
    path("detail/<int:pk>/", views.ProductDetail.as_view(), name="detail"),
    path("delete/<int:pk>/", views.DeleteProduct.as_view(), name="delete"),
]