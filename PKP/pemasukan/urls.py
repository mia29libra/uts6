from django.urls import path
from . import views

urlpatterns = [
    path('pemasukan/', views.pemasukan_list),
]