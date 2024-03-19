from django_celery.tasks import my_task
from django.http import HttpResponse

def home(request):

    print("in here")
    result = my_task.delay(3, 5)
    print(result)
    return HttpResponse(f"Task id: {result.id}")