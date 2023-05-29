from django.shortcuts import render
from .models import Profile

# Create your views here.

def First(request):
    user_prof = Profile.objects.all()

    return render(request, 'first/First.html', locals())


def Create(request):

    return render(request, 'first/create.html', locals())
