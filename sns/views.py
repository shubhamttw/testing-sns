from django.shortcuts import render
from django_sns_view.views import SNSEndpoint
from .models import Text
import json
from django.http.response import JsonResponse
# Create your views here.


class ReceiveSnsMessage(SNSEndpoint):

    def handle_message(self, message, payload):
        message = json.loads(message)
        text = message.get('text')
        if text:
            Text.objects.create(text=text)
        else:
            Text.objects.create(text='Error: Did not received any text')
    
    def get(self, request, *args, **kwargs):
        return JsonResponse(data={'message':'View to receive sns message'})




