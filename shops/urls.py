from django.urls import path
from . import views

urlpatterns = [
  path('',views.main,name='main'),
  path('index/',views.IndexView.as_view(),name='index'),
  path(
        "detail/<int:detail_id>/",
        views.ItemDetailView.as_view(), 
        name = 'item-detail'),
  path('mybag/',views.MybagView.as_view(),name='mybag'),
  path('mybag/<int:cloth_id>/delete',views.cart_delete, name='cart-delete'),
  path('detail/<int:cloth_id>/add',views.cart_add, name='cart-add'),
]