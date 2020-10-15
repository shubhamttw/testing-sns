from django.urls import path
from .views import ReceiveSnsMessage

urlpatterns = [
    path('receive-sns/', ReceiveSnsMessage.as_view())
]