from django.db import models

class Content(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=False, default='')
    text = models.TextField()

    class Meta:
        ordering = ['created']
