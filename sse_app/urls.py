from django.urls import path
from .views import sse_stream

urlpatterns = [
    path('', sse_stream, name='sse_stream'),
]