from django.shortcuts import render
from .models import Choice
# Create your views here.

def Home(request):
    choices = Choice.objects.all()
    return render(request, "base.html", {'choices': choices})


