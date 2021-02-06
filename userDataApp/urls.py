from django.urls import path
from .views import userDataPage

urlpatterns = [
    path('user/<str:primary_key>/userdata/', userDataPage, name="userDataPage_url")
]