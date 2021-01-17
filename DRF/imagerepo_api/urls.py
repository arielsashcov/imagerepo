from .views import ImageList, ImageDetail, ImageListDetailfilter, CreateImage, EditImage, AdminImageDetail, DeleteImage
from django.urls import path

app_name = 'imagerepo_api'

urlpatterns = [
    path('', ImageList.as_view(), name='listimage'),
    path('image/<str:pk>/', ImageDetail.as_view(), name='detailimage'),
    path('search/', ImageListDetailfilter.as_view(), name='searchimage'),
    # Image Admin URLs
    path('admin/create/', CreateImage.as_view(), name='createimage'),
    path('admin/edit/imagedetail/<int:pk>/',
         AdminImageDetail.as_view(), name='admindetailimage'),
    path('admin/edit/<int:pk>/', EditImage.as_view(), name='editimage'),
    path('admin/delete/<int:pk>/', DeleteImage.as_view(), name='deleteimage'),
]
