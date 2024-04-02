from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['POST'])
def postmethod(request):
    objectone = promotiontable.objects.all()
    serilizer = promotion_serilizer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
    return Response(serilizer.validated_data)

@api_view(['PUT'])
def updatemethod(request,id):
    objecttwo = promotiontable.objects.get(id = id)
    serilizer = promotion_serilizer(instance= objecttwo, data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data)

@api_view(['GET'])
def getmethod(request):
    getobject = promotiontable.objects.all()
    serilizer = promotion_serilizer(getobject, many=True)
    return Response(serilizer.data)


@api_view(['GET'])
def hrgetmethod(request):
    getobject = promotiontable.objects.all()
    serilizer = hr_serilizer(getobject, many=True)
    return Response(serilizer.data)