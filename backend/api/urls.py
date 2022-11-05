#!/usr/bin/env python3

from django.urls import path

from . import views



urlpatterns = [
    path('bank_name/',views.bank_name_by_id),
    path('details/',views.all_details),
]
