from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import time
import json
from .thread import *
# Create your views here.
async def home(request):
    # for i in range(1,10):
    #     channel_layer = get_channel_layer()
    #     data = {'count':i}
    #     await (channel_layer.group_send)('new_consumer_group', {'type':'send_notification', 'value':json.dumps(data)})

    #     time.sleep(1)

    return render(request, 'home.html')

# def send_notification(request):
#     notification = Notification.objects.create(notification='Hello World')
#     return redirect('home')
from django.http import JsonResponse
def generate_student_data(request):
    total=request.GET.get('total')
    CreateStudentsThread(int(total)).start()
    return JsonResponse({'status':'success 200'})
    