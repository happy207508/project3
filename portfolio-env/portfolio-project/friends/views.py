from django.shortcuts import render
from .models import animal2
# Create your views here.
def home(request):
	animal2 = animal2.objects
	return render(request, 'home.html', {'animal2':animal2})