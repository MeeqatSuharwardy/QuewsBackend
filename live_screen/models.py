from django.db import models

class LiveVideo(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    is_live = models.BooleanField(default=False)

    def __str__(self):
        return self.title
