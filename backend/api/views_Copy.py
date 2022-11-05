from django.shortcuts import render

from django.forms.models import model_to_dict
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view



from django.http import JsonResponse

from api.models import Banks,Branches
from api.serializers import bank_name_by,branch_details

import json

@api_view(["GET"])
def bank_name_by_id(request, *args, **kwargs):
    if request.method != "GET":
        return Response({"deatil" : "Only GET method was available for reading the data \n The user was only allowed to see the data :)"},status=405)
    instance =Banks.objects.all().order_by("?").first()
    data = {}
    if instance:
        #data=model_to_dict(instance,fields=['id','name'])
        data = bank_name_by(instance).data
    return Response(data)


@api_view(["GET"])
def all_details(request, *args, **kwargs):
    if request.method != "GET":
        return Response({"deatil" : "Only GET method was available for reading the data \n The user was only allowed to see the data :)"},status=405)
    instance =Branches.objects.all().order_by("?").first()
    data = {}
    if instance:
        data=branch_details(instance).data
    return Response(data)
