from django.shortcuts import render
from django.urls import reverse
from allauth.account.views import PasswordChangeView
from django.views.generic import RedirectView
from django.views.generic import ListView, DetailView
from shops.models import Cloth
# Create your views here.

def main(request):
    return render(request,'shops_base/base.html')

def item_detail(request):
    return render(request,'shops/detail.html')

def mybag(request):
    return render(request,'shops/mybag.html')

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
    
