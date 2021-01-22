from django.shortcuts import render

# Create your views here.
from home.models import AllTask
def index(request):
    tasks = AllTask.objects.all()
    dict = {
        'tasks' : tasks,
    }
    return render(request, 'index.html', dict)