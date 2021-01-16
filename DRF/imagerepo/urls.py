from django.urls import path
from django.views.generic import TemplateView

app_name = 'imagerepo'

urlpatterns = [
    path('', TemplateView.as_view(template_name="imagerepo/index.html")),
]
