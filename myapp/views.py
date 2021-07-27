from django.shortcuts import render
from rest_framework.views import APIView
import json
from django.http.response import JsonResponse
from .tasks import send_email
from rest_framework import status

# Create your views here.

class SendEmail(APIView):

    def post(self, request):
        payload = json.loads(request.body)

        email = payload["email"]
        send_email.delay(email)

        return JsonResponse(status=status.HTTP_200_OK, data={"successful": "sent to celery"})
