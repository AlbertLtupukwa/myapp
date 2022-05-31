from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    body = models.TextField()
    created = models.TimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

        def __str__(self):
            return self.name