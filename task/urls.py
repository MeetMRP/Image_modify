from django.urls import path
from .views import *

urlpatterns = [
      path('api/register/', RegisterApi.as_view()),
      path('api/image/', ImageApi.as_view()),
]