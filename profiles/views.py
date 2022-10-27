from django.views.generic import TemplateView, View, DetailView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import JsonResponse, HttpResponseBadRequest
from .models import Product
from cart.models import Cart

from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings


from profiles.models import Profile

class ProfileView(LoginRequiredMixin, DetailView):
    http_method_names = ["get"]
    template_name = "profiles/detail.html"
    model = Profile
    context_object_name = "profile"

class UpdateProfile(LoginRequiredMixin, UpdateView):
    # specify the model you want to use
    model = User
    template_name = "profiles/update.html"
  
    # specify the fields

    fields = [
        "first_name",
        "last_name",
        "email",
        "username",
    ]
    success_url="../profile-update-image/"


class UpdateProfileImage(LoginRequiredMixin, UpdateView):
    # specify the model you want to use

    model = Profile
    template_name = "profiles/update-image.html"

    fields = [
        "image",
        "address",
    ]
    success_url="../"
  


# Create your views here.
class CartPage(LoginRequiredMixin,TemplateView):
    http_method_names = ["get"]
    template_name = "profiles/cart.html"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cart_list = list(
                Cart.objects.filter(added_by=self.request.user).values_list('added_product', flat=True)
        )
        products = Product.objects.filter(id__in=cart_list).order_by('-id')[0:30]
        context['cart_list'] = products
        return context




class AddCartView(LoginRequiredMixin, View):
    http_method_names = ["post"]
    def post(self, request, *args, **kwargs):
        data = request.POST.dict()
        

        if "action" not in data or "product" not in data:
            return HttpResponseBadRequest("Missing data")

        try:
            product = Product.objects.get(name=data['product'])
        except Product.DoesNotExist:
            return HttpResponseBadRequest("Missing product")

        if data['action'] == "add-item":
            # Follow
            cart, created = Cart.objects.get_or_create(
                added_by=request.user,
                added_product=product
            )
            messages.add_message(request, messages.INFO, 'Item added to the cart')
        else:
            # Unfollow
            try:
                cart = Cart.objects.get(
                    added_by=request.user,
                    added_product=product,
                )
            except Cart.DoesNotExist:
                cart = None

            if cart:
                
                cart.delete()
                messages.add_message(request, messages.INFO, 'Item removed fron the cart')


        return JsonResponse({
            'success': True,
            'wording': "Remove" if data['action'] == "add-item" else "Add to cart"
        })

class RemoveCartView(LoginRequiredMixin, View):
    http_method_names = ["post"]
    model=Cart
    def post(self, request, *args, **kwargs):
        data = request.POST.dict()
        try:
            product = Product.objects.get(name=data['product'])
        except Product.DoesNotExist:
            return HttpResponseBadRequest("Missing product")
        try:
            cart = Cart.objects.get(
                added_by=request.user,
                added_product=product,
            )

        except Cart.DoesNotExist:
            cart = None

        if cart:
            cart.delete()
        return JsonResponse({
            'success': True,
        })

