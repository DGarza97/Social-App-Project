from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name="conversations")
    updated_at = models.DateTimeField(auto_now=True)

    def other_user(self, user):
        return self.participants.exclude(id=user.id).first()

    def last_message(self):
        last = self.messages.order_by("-created_at").first()
        return last.content if last else None

    def __str__(self):
        return f"Conversation {self.id}"


class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation,
        related_name="messages",
        on_delete=models.CASCADE
    )
    sender = models.ForeignKey(
        User,
        related_name="sent_messages",
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.id}"
