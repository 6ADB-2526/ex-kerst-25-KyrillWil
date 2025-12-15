from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.

def test(request):
    return HttpResponse('test')
