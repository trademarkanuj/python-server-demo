from django.db import models
class Message(models.Model):
    role=models.CharField(max_length=10)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=["created_at"]
