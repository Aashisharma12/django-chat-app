from django.shortcuts import render
from django.conf import settings

def map(request):
    key = settings.GOOGLE_API_KEY
    context = {
        'key':key,
    }
    return render(request, 'google/map.html',context)
