from django.shortcuts import render, HttpResponse, get_object_or_404, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonSerializer
from .models import Person


class PersonList(APIView):

    def get(self, request):
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
