from django.contrib import admin
from django.urls import path 

from lenovo import views 
urlpatterns=[path('admin/',admin.site.urls),
path('',views.index,name ="homepage"),
path('contact/',views.contact_views),
path('articl/',views.articles_views),
path('panier/',views.panier_views),
path('categorie/',views.categorie_views),]
