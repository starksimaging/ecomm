from django.shortcuts import render
from .models import Shoe

# Create your views here.

def home(request):
    shoes = Shoe.objects.all()
    return render(request, 'home.html', {'shoes': shoes})