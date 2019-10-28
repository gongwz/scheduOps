# Create your views here.

from django.http import JsonResponse
from scheduapp import tasks
import time


# Create your views here.

def index(request, *args, **kwargs):
    res = tasks.add.delay(2, 3)
    # 任务逻辑
    print('res===>', res)
    
    return JsonResponse({'status': 'successful', 'task_id': res.task_id})