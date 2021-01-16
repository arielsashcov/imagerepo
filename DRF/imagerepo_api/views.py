from rest_framework import generics
from imagerepo.models import Image
from .serializers import ImageSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class ImageUserWritePermission(BasePermission):
    message = 'Editing images is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class ImageList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ImageSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Image, slug=item)

    # Define Custom Queryset
    def get_queryset(self):
        return Image.objects.all()


class ImageDetail(generics.RetrieveAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        slug = self.request.query_params.get('slug', None)
        print(slug)
        return Image.objects.filter(slug=slug)


class ImageListDetailfilter(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']


class ImageSearch(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']
