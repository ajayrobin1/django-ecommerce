from django.views.generic import CreateView, TemplateView, DetailView, View
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest

from cart.models import Cart
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages


# Create your views here.
class HomePage(TemplateView):
    http_method_names = ["get"]
    template_name = "product/homepage.html"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        products = Product.objects.all().order_by('-id')[0:30]
        print(len(products))
        if len(products)==0:
            empty=True
        else:
            empty=False
        context['products'] = products
        context['empty'] = empty
        return context

class CreateProduct(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "product/sell.html"
    fields=['name', 'image', 'price', 'discription']
    success_url = "/"
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.seller = self.request.user
        obj.save()
        return super().form_valid(form)

class DeleteProduct(LoginRequiredMixin, View):
    model = Product
    def post(self, request, *args, **kwargs):
        data = request.POST.dict()
        try:
            product = Product.objects.get(name=data['product'])
        except Product.DoesNotExist:
            return HttpResponseBadRequest("Missing product")
        if self.request.user.is_authenticated:
            messages.add_message(request, messages.INFO, product.name + ' removed from the site')
            product.delete()
            
        return JsonResponse({
            'success': True,
        })


       

class ProductDetail(DetailView):
    http_method_names = ["get","post"]
    template_name = "product/detail.html"
    model = Product
    context_object_name = "product"
    def get_context_data(self, **kwargs):
        product = self.get_object()
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            val= Cart.objects.filter(added_product=product, added_by=self.request.user).exists()
            context['in_cart'] =val
            if product.seller == self.request.user:
                context['buy_link'] =False
            else:
                context['buy_link'] =True

        return context