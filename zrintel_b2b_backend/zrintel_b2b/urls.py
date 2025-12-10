from django.urls import path
from .views import register_supplier

urlpatterns = [
    path("register/", register_supplier, name="register_supplier"),
]
