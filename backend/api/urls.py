#!/usr/bin/env python3

from django.urls import path,re_path

from . import views



urlpatterns = [

    #Retrive bank name by id   eg: ["http://localhost:8000/api/2"]
    path('<int:pk>/',views.bank_name_id),

    #retrive complete bank details by IFSC  eg: ["http://localhost:8000/api/details/ABHY0065001"]
    path('details/<str:pk>/',views.bank_details_by_ifsc),

    #list all the banks and the ID  eg: ["http://localhost:8000/api/list/"]
    path('list/',views.bank_list_name),

    #list complete details of all the banks eg: ["http://localhost:8000/api/list_all/"]
    path('list_all/',views.bank_list),

    #filter banks using branches eg: ["http://localhost:8000/api/bank_branch/RTGS-HO"]
    path("bank_branch/<str:pk>",views.bank_by_branch),

]
