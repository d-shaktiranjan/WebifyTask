from django.shortcuts import render, redirect

# Create your views here.
from home.models import AllTask
from datetime import datetime
from home.mixSlug import getSlug


def index(request):
    tasks = AllTask.objects.all()
    dict = {
        'tasks': tasks,
    }
    if request.method == "POST":
        name = request.POST.get('name')
        about = request.POST.get('about')
        date = request.POST.get('date')
        slug = getSlug(name, about)
        addNew = AllTask(taskName=name, about=about, sColor="warning",
                         status="Init", dateTime=datetime.now(), slug=slug, subDateTime=date)
        addNew.save()
        return redirect("index")
    return render(request, 'index.html', dict)


def wip(request, slug):
    update = AllTask.objects.get(slug=slug)
    update.status = "WIP"
    update.sColor = "primary"
    update.save()
    home = redirect("/")
    return home


def finish(request, slug):
    update = AllTask.objects.get(slug=slug)
    update.status = "Finish"
    update.sColor = "success"
    update.save()
    home = redirect("/")
    return home


def delete(request, slug):
    update = AllTask.objects.get(slug=slug)
    update.delete()
    home = redirect("/")
    return home
