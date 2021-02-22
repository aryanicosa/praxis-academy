from django.shortcuts import render

from .models import Registrasi

# Create your views here.
def index(request):
    return render(request, 'index.html')

def regist(request):
    registrasi = Registrasi.objects.all()
    context = {
        'registrasi': registrasi
    }
    return render(request, 'registrasi.html', context)

def info(request):
    return render(request, 'info.html')