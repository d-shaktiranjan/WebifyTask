from django.db import models

# Create your models here.
class AllTask(models.Model):
    taskName = models.CharField(max_length=10)
    about = models.CharField(max_length=25)
    dateTime = models.DateTimeField()
    subDateTime = models.DateTimeField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.taskName
    