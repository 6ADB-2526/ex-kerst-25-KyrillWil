from django.urls import path
from . import views

urlpatterns = [
    path('welkom/', views.welkom),
    path('addGebruiker/', views.addUser),
    path('alleGebruikers/', views.showUsers),
    path('bewerkGebruiker/<int:id>', views.bewerkUser),
    path('deleteGebruiker/<int:id>', views.deleteUser),
    path('gebruikerId/<int:id>', views.gebruikerId),
    path('gebruikerLogins/', views.userLogin)
]