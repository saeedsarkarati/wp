from django.urls import path
from .views import Bank_get, index

urlpatterns = [
    path('', index, name='index'),
    path('list', Bank_get.as_view()),
]