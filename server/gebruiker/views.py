from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.


# hoe ga je hier connectie maken met je datamodel?
# Het was niet de bedoeling dat je 2x een app ging maken. in 1 app moest je het onderscheid maken tussen user en admin. 
# je maakt het jezelf moeilijk hierdoor.


def test(request):
    return HttpResponse('test')
