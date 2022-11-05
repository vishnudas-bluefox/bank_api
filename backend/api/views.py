from rest_framework import generics

from .models import Banks,Branches
from .serializers import bank_name_by,branch_details

#retrive bank name by id
class bank_name_by_id(generics.RetrieveAPIView):
    queryset = Banks.objects.all()
    serializer_class = bank_name_by
    lookup_field = 'pk'
    print(lookup_field)
    #Banks.objects.get(pk=1)

bank_name_id = bank_name_by_id.as_view()

#retrive bank details by ifsc
class bank_details_by_ifsc(generics.RetrieveAPIView):
    queryset = Branches.objects.all()
    serializer_class = branch_details

    #lookup_field = 'pk
    #Branhes.objects.get(pk=1)

bank_details_by_ifsc = bank_details_by_ifsc.as_view()


#retrive all bank details by ifsc
class bank_list(generics.ListAPIView):
    queryset = Branches.objects.all()
    serializer_class = branch_details


bank_list = bank_list.as_view()


#retrive all bank name and id
class bank_list_name(generics.ListAPIView):
    queryset = Banks.objects.all()
    serializer_class = bank_name_by


bank_list_name = bank_list_name.as_view()
