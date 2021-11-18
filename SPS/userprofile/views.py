from django.shortcuts import render
from .models import Profile
# Create your views here.

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'index.html', {'profiles':profiles})
