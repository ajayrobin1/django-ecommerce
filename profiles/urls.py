from django.urls import path

from . import views

app_name = "profile"

urlpatterns = [
    path("<int:pk>/cart/", views.CartPage.as_view(), name="cart"),
    path("<int:pk>/addcart/", views.AddCartView.as_view(), name="addcart"),
    path("<int:pk>/remove/", views.RemoveCartView.as_view(), name="remove"),
    path("<int:pk>/", views.ProfileView.as_view(), name="detail"),
    path("<int:pk>/profile-update/", views.UpdateProfile.as_view(), name="update"),
    path("<int:pk>/profile-update-image/", views.UpdateProfileImage.as_view(), name="update_image"),
]