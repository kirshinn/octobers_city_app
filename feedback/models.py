from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

class Feedback(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.subject} from {self.user.username if self.user else 'Anonymous'}"
