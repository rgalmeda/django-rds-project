from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework import viewsets
from books.models import Book
from django.views import View

# Create your views here.

class BookCreateView(View):
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=ret.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


