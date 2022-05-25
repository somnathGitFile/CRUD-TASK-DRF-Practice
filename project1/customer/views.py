from msilib.schema import Class
from django.shortcuts import render
from customer.serializers import CustomerSerializer
from .models import Customer
from rest_framework import viewsets

# Create your views here.
class customerDetails(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
