from django.urls import path
from .views import ListAgencies

urlpatterns = [
    path('', ListAgencies.as_view(), name="list"),
]