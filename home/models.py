from django.db import models

# Create your models here.
class AllTask(models.Model):
    taskName = models.CharField(max_length=30)
    about = models.CharField(max_length=50)
    dateTime = models.DateTimeField()
    subDateTime = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10)
    slug = models.CharField(max_length=80)

    def __str__(self):
        return self.taskName
    