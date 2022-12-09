from django.http import HttpResponse
from django.shortcuts import render
from .db_articles import articles


def index(request):
  # return HttpResponse("hellow,wordhow are yous")
  return render(request,'acceuill.html')




   
def contact_views(request):
  # return HttpResponse("contactez nous")
  return render(request,'cantact.html')

def articles_views(request):
   return render(request,'articl.html',context={'articl':articles})
def panier_views(request):
 return render(request,'panier.html')
def categorie_views(request):
 return render(request,'categorie.html')

   

  





