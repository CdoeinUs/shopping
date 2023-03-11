from django.urls import path
from . import views

urlpatterns = [
  path('',views.main,name='main'),
  path('index/',views.IndexView.as_view(),name='index'),
  path(
        "detail/<int:detail_id>/",
        views.ItemDetailView.as_view(), 
        name = 'item-detail'),
  path('mybag/',views.mybag,name='mybag'),
]