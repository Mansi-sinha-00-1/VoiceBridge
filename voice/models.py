from django.db import models
from django.contrib.auth.models import User

# class VoiceHistory(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     audio_file = models.FileField(upload_to='audio/')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.text[:50]

class VoiceHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    audio_file = models.FileField(upload_to='audio/', null=True, blank=True)
    source = models.CharField(max_length=20, default='text')  
    mode = models.CharField(max_length=20, default="accent")
    language = models.CharField(max_length=10, default="en")
    created_at = models.DateTimeField(auto_now_add=True)