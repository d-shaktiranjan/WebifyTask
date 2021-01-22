from django.shortcuts import render

# Create your views here.
from home.models import AllTask
from datetime import datetime
def index(request):
    tasks = AllTask.objects.all()
    dict = {
        'tasks' : tasks,
    }
    if request.method == "POST":
        name = request.POST.get('name')
        about = request.POST.get('about')
        date = request.POST.get('date')
        addNew = AllTask(taskName = name, about = about, subDateTime = datetime.now(), status = "Init", dateTime = datetime.now())
        addNew.save()
    return render(request, 'index.html', dict)