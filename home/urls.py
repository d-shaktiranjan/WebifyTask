from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name = "index"),
    path('wip/<slug:slug>',views.wip, name = "wip"),
    path('finish/<slug:slug>',views.finish, name = "finish"),
    path('delete/<slug:slug>',views.delete, name = "delete"),
]