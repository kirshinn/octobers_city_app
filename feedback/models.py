from django.db import models
from django.utils import timezone
from core.models import Status
from accounts.models import CustomUser

class Feedback(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    answer = models.TextField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=None, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.subject} from {self.user.username if self.user else 'Anonymous'}"
