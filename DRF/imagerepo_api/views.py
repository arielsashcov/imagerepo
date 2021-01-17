from django.shortcuts import get_object_or_404
from imagerepo.models import Image
from .serializers import ImageSerializer
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

# View Images


class ImageList(generics.ListAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class ImageDetail(generics.RetrieveAPIView):

    serializer_class = ImageSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Image, slug=item)

# Search Images


class ImageListDetailfilter(generics.ListAPIView):

    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_backends = [filters.SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' search.
    # '$' iregex.
    search_fields = ['^slug']


# Admin Image
class CreateImage(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class AdminImageDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class EditImage(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class DeleteImage(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


""" Concrete View Classes
# CreateAPIView
Used for create-only endpoints.
# ListAPIView
Used for read-only endpoints to represent a collection of model instances.
# RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
# DestroyAPIView
Used for delete-only endpoints for a single model instance.
# UpdateAPIView
Used for update-only endpoints for a single model instance.
# ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
# RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
# RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""
