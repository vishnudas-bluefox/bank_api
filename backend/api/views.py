from django.shortcuts import render

from django.forms.models import model_to_dict
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import JsonResponse

from api.models import Banks,Branches
import json

@api_view("GET")
def api_home(request, *args, **kwargs):
    if request.method != "GET":
        return Response({"deatil" : "Only GET method was available for reading the data \n The user was only allowed to see the data :)"},status=405)
    model_data =Banks.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data=model_to_dict(model_data,fields=['id','name'])

    return JsonResponse(data)
