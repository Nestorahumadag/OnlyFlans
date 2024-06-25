from django.shortcuts import render
from .models import Flan 

# Create your views here.
def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, "index.html", {'flanes': flanes_publicos})

def acerca(request):
    return render(request, "about.html")

def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    user_name = request.GET.get('name', 'cliente')
    return render(request, "welcome.html", {'user_name': user_name, 'flanes': flanes_privados})