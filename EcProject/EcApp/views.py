from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def accueil(request):
    contexte ={"message":"Hey salut!!"}
    return render(request,'accueil.html', contexte)

def index(request):
    return render(request,'index.html')

# def pagedevente(request):
#     contexte = {}
#     template = loader.get_template("EcApp/pagedevente.html")
#     return HttpResponse(template.render(contexte,request))
