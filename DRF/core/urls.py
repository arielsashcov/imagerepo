from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # API Token Management
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Project URLs
    path('admin/', admin.site.urls),
    path('', include('imagerepo.urls', namespace='imagerepo')),

    # User Management
    path('api/user/', include('users.urls', namespace='users')),

    # imagerepo_api Application
    path('api/', include('imagerepo_api.urls', namespace='imagerepo_api')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # API schema and Documentation
    # path('project/docs/', include_docs_urls(title='ImageRepoAPI')),
    # path('project/schema', get_schema_view(
    #     title="ImageRepoAPI",
    #     description="API for the ImageRepoAPI",
    #     version="1.0.0"
    # ), name='openapi-schema'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
