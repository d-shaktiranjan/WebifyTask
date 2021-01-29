from django.shortcuts import render, redirect

# Create your views here.
from home.models import AllTask
from datetime import datetime
from home import mixSlug
def index(request):
    tasks = AllTask.objects.all()
    dict = {
        'tasks' : tasks,
    }
    if request.method == "POST":
        name = request.POST.get('name')
        about = request.POST.get('about')
        date = request.POST.get('date')
        slug = mixSlug(name, about)
        addNew = AllTask(taskName = name, about = about, subDateTime = datetime.now(), status = "Init", dateTime = datetime.now(), slug = slug)
        addNew.save()
    return render(request, 'index.html', dict)

def wip(request, slug):
    update = AllTask.objects.get(slug=slug)
    update.status = "WIP"
    update.save()
    home = redirect("/")
    return home