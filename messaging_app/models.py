from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messaging_sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messaging_received_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class MessageReaction(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="reactions")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    emoji = models.CharField(max_length=10)  # تخزين الإيموجي كـ Unicode
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('message', 'user')  # كل مستخدم يضيف تفاعل واحد فقط على كل رسالة

    def __str__(self):
        return f"{self.user.username} reacted to {self.message.id} with {self.emoji}"
