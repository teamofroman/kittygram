from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cat
from .serializers import CatSerializer


@api_view(['GET', 'POST'])
def cat_list(request):
    if request.method == 'POST':
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    cats = Cat.objects.all()
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def hello(request):
    if request.method == 'POST':
        return Response(
            {
                'message': 'POST method',
                'data': request.data,
            },
            status=status.HTTP_200_OK,
        )

    return Response({'message': 'GET method'}, status=status.HTTP_200_OK)


class APICatCR(APIView):
    def get(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APICatRUD(APIView):
    def get(self, request, id):
        try:
            cat = Cat.objects.get(id=id)
        except Exception:
            cat = None

        if cat is None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = CatSerializer(cat)
        return Response(serializer.data)

    def delete(self, request, id):
        try:
            cat = Cat.objects.get(id=id)
            cat.delete()
        except Exception:
            pass

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        try:
            cat = Cat.objects.get(id=id)
        except Exception:
            cat = None

        if cat is None:
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = CatSerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            cat = Cat.objects.get(id=id)
        except Exception:
            cat = None

        if cat is None:
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
