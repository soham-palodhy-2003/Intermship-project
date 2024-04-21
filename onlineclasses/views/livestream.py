from cv2 import VideoCapture
from django.shortcuts import render, HttpResponse 
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync  
import cv2
import pyaudio
import wave
import os
import threading
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from onlineclasses.models import UserProfile

@login_required
def streaming_view(request):
    print(threading.get_native_id())
    user_profile = UserProfile.objects.get(user=request.user)
    username = user_profile.user.username
    print(username)

    context = {
        'username': username,
    }
    return render(request, 'courses/index.html',context)
def chat_view(request, room_name):
    user_profile = UserProfile.objects.get(user=request.user)
    username = user_profile.user.username
    print(username)
    return render(request, 'courses/streaming.html', {
        'room_name': room_name,
        'username': username,
    })
   
def streaming_message(event):

    message = event['message']

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'streaming_group',
        {
            'type': 'chat_message',
            'message': message,
        }
    )

def chat_message(event):
    message = event['message']

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'chat_group',
        {
            'type': 'chat_message',
            'message': message,
        }
    )