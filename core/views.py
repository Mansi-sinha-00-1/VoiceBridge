import os
from django.conf import settings
from django.shortcuts import render

def home(request):
    print("Template path:", os.path.join(settings.BASE_DIR, 'templates'))
    return render(request, 'index.html')