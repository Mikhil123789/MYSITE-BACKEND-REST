from myapp.models import ClientRequest
from rest_framework import serializers

# class RequestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ClientRequest
#         fields = "__all__"


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientRequest
        fields = "__all__"