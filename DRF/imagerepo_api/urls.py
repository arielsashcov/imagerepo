from .views import ImageList
from rest_framework.routers import DefaultRouter

app_name = 'imagerepo_api'

router = DefaultRouter()
router.register('', ImageList, basename='image')
urlpatterns = router.urls
