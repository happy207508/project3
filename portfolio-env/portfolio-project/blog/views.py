from django.shortcuts import render

from .models import animal1
# Create your views here.
def allblogs(request):
	animal1 = animal1.objects
	return render(request, 'allblogs.html', {'animal1':animal1})