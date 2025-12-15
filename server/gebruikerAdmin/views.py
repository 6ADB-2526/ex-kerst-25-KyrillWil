from django.shortcuts import render  # waarom importeer je render? 
from django.http import HttpResponse, JsonResponse
import json
from .models import gebruikers
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Create your views here.

#test pagina
def welkom(request):
    return HttpResponse('welkom')

#gebruiker toevoegen
@csrf_exempt
def addUser(request):
    post_data =  json.loads(request.body.decode('utf-8'))
    newUser = gebruikers()
    newUser.login = post_data["login"]
    newUser.password = post_data["password"]
    newUser.email = post_data["email"]

    # mocht je in je model defaults gebruikt hebben zijn onderstaande zaken niet noodzakelijk
    newUser.role = post_data["role"]
    newUser.isSuperuser = post_data["isSuperuser"]
    newUser.save()
    return JsonResponse(model_to_dict(newUser))

#toon alle gebruikers
def showUsers(request):
    users = gebruikers.objects.all().values()
    returnUser = list(users)
    return JsonResponse(returnUser, safe=False)

#gebruiker aanpassen met id
@csrf_exempt
def bewerkUser(request, id):
    post_data =  json.loads(request.body.decode('utf-8'))
    userId = gebruikers.objects.get(pk = id)
    userId.login = post_data["login"]
    userId.password = post_data["password"]
    userId.email = post_data["email"]
    userId.role = post_data["role"]
    userId.isSuperuser = post_data["isSuperuser"]
    userId.save()
    return JsonResponse(model_to_dict(userId))

#gebruiker verwijder met id
@csrf_exempt
def deleteUser(request, id):
    # waarom heb je hier post_data nodig terwijl je het niet gebruikt.
    # Een delete doe je niet via url-variabelen. Dit is te riskant.
    post_data =  json.loads(request.body.decode('utf-8'))
    userId = gebruikers.objects.get(pk = id)
    userId.delete()
    return JsonResponse({'status': 'gelukt'})

#gebruiker vinden met id
def gebruikerId(request, id):
    userId = gebruikers.objects.get(pk = id)
    return JsonResponse(model_to_dict(userId))

#alleen logins tonen
def userLogin(request):
    # wat ben je met Login als je geen ID hebt. Wat wil je hier verder mee doen? 
    users = gebruikers.objects.all().values("login")
    returnUser = list(users)
    return JsonResponse(returnUser, safe=False)

# controle van login in combinatie met wachtwoord kan ik niet terugvinden. 



