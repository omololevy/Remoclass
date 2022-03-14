from django.urls import path
from base import views

urlspatterns = [
    path('api/units', views.unit_list),
    # path('api/units/<int:pk>', views.units_detail),
]