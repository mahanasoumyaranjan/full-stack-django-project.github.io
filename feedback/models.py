from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    feed = models.TextField()
    date_time = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.name
