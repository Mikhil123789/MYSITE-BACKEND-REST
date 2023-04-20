from django.shortcuts import render
from myapp.models import ClientRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RequestSerializer
from rest_framework import generics
# Create your views here.

class MyView(APIView):
    serializer_class = RequestSerializer
    def get(self, request):
        object_ = ClientRequest.objects.all()
        serializer= RequestSerializer(object_, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "successfully created new request"})
        else:
            # Return a response with errors
            return Response(serializer.errors, status=400)

class PostSomething(generics.CreateAPIView):
    serializer_class = RequestSerializer # here
    # permission_classes = (AllowAny,)
    allowed_methods = ('POST',)
    
        