import json
import requests
from django.shortcuts import render
from django.http import HttpResponse


def form_message(request):
    return render(request, "service.html")


def send_msg(request):
    msg = request.GET["msg"]
    send_notification("Alerta de Accidente", msg, "APP_ACCIDENT")
    message = "Message has been sent."
    return HttpResponse(message)


def send_notification(message_title, message_desc, topic):
    fcm_api = "AAAA9H78OD0:APA91bHsHHs9nyv1O51iM2bgOh51GTZ9U_Xr0efHxhpDR5OClb3vfoNGZyGEJNxJViSQbc1CkBeFJvcdVCIcsqsh0qFotxk29L8IPdsSATcftmMZL8Q5WeZi1H2ibdbgucp4bKWGoZD-"
    url = "https://fcm.googleapis.com/fcm/send"

    headers = {
        "Content-Type": "application/json",
        "Authorization": 'key=' + fcm_api
    }

    payload = {
        "to": "/topics/"+topic,
        "priority": "high",
        "notification": {
            "body": message_desc,
            "title": message_title,
            "image": "https://cdn-icons-png.flaticon.com/512/3209/3209005.png",
            "icon": "https://cdn-icons-png.flaticon.com/512/3209/3209005.png",
        }
    }

    requests.post(url, data=json.dumps(payload), headers=headers)
