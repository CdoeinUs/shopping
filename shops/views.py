from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from allauth.account.views import PasswordChangeView
from django.views.generic import RedirectView
from django.views.generic import ListView, DetailView
from shops.models import Cloth,User
from django.db import models
# Create your views here.

def main(request):
    return render(request,'shops_base/base.html')

def item_detail(request):
    return render(request,'shops/detail.html')

class MybagView(ListView):
    model = User
    template_name = "shops/mybag.html"
    context_object_name = 'mybag'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        total_price = user.cart.aggregate(total_price=models.Sum('price'))['total_price'] or 0
        context['total_price'] = total_price
        return context    
    

class ItemDetailView(DetailView):
    model = Cloth
    template_name ="shops/detail.html"
    pk_url_kwarg = 'detail_id'
    
class IndexView(ListView):
    model = Cloth
    template_name = "shops/index.html"
    context_object_name = 'products'
    paginate_by = 4
    ordering = ["-dt_created"]
    
    
class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self) :
        return reverse("index")
    
def cart_delete(request, cloth_id):
    user = request.user
    cloth = Cloth.objects.get(id = cloth_id)
    user.cart.remove(cloth)
    return redirect('mybag')

def cart_add(request, cloth_id):
    user = request.user
    cloth = Cloth.objects.get(id = cloth_id)
    user.cart.add(cloth)
    return redirect('item-detail',cloth_id)