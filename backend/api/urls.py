#!/usr/bin/env python3

from django.urls import path

from . import views



urlpatterns = [
    #path('bank_name/',views.bank_name_by_id),
    #path('details/',views.all_details),

    #Retrive bank name by id
    path('<int:pk>/',views.bank_name_id),

    #retrive complete bank details by IFSC
    path('details/<str:pk>/',views.bank_details_by_ifsc),

    #list all the banks and the ID
    path('list/',views.bank_list_name),

    #list complete details of all the banks
    path('list_all/',views.bank_list),

]
