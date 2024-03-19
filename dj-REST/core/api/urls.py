from django.urls import path
from home.views import index,person

urlpatterns=[
    path('index/',index),
    path('person/',person),
]