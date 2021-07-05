from django.db import models


class NotesModel(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image_url = models.URLField()

