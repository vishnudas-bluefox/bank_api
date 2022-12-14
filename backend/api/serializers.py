

from rest_framework import serializers

from api.models import Banks,Branches


# for retriving bank names using id
class bank_name_by(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = [
            'name',
            'id',

        ]

# retrive all the data from the table branches
class branch_details(serializers.ModelSerializer):
    class Meta:
        model =Branches
        fields =[
            'ifsc',
            'bank',
            'branch',
            'address',
            'city',
            'district',
            'state',

        ]
