from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoSerializer, UserSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def osoba_detail(request, pk):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Osoba
    :return: Response (with status and/or object/s data)
    """
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Osoba.
    """
    if request.method == 'GET':
        osoba = Osoba.objects.get(pk=pk)
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_update_delete(request, pk):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Person
    :return: Response (with status and/or object/s data)
    """
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(wlasciciel=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def osoba_list(request):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    """
    Lista wszystkich obiektów modelu Person.
    """
    if request.method == 'GET':
        nazwisko = request.query_params.get('nazwisko')
        if nazwisko:
            osoby = Osoba.objects.filter(nazwisko__contains=nazwisko)
        else:
            osoby = Osoba.objects.all().order_by('id')
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(['GET', 'PUT', 'DELETE'])
def stanowisko_detail(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Stanowisko
    :return: Response (with status and/or object/s data)
    """
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Stanowisko.
    """
    if request.method == 'GET':
        stanowisko = Stanowisko.objects.get(pk=pk)
        serializer = StanowiskoSerializer(stanowisko)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StanowiskoSerializer(stanowisko, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def stanowisko_list(request):
    """
    Lista wszystkich obiektów modelu Stanowisko.
    """
    if request.method == 'GET':
        stanowiska = Stanowisko.objects.all()
        serializer = StanowiskoSerializer(stanowiska, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StanowiskoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer