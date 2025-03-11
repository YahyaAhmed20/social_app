from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from datetime import timedelta

User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_received_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)  # Flag لحذف الرسالة
    
    
    

    
    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.content[:30]}"
    def can_be_deleted(self):
        return now() - self.timestamp <= timedelta(minutes=5)  # يقدر يحذفها خلال 5 دقائق

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    last_seen = models.DateTimeField(auto_now=True)  # تحديث تلقائي عند كل تعديل

    def __str__(self):
        return f"{self.user.username} - Last Seen: {self.last_seen}"