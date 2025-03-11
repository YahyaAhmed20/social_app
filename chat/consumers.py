import json
from datetime import datetime
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async
from .models import Message, UserProfile

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        if self.user.is_authenticated:
            await self.update_last_seen()
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        await self.update_last_seen()

    async def receive(self, text_data):
        data = json.loads(text_data)
        event_type = data.get("event")

        if event_type == "delete_message":
            message_id = data["message_id"]
            message = await sync_to_async(Message.objects.get)(id=message_id)

            if message.sender == self.user and message.can_be_deleted():
                message.deleted = True
                await sync_to_async(message.save)()

                await self.send(text_data=json.dumps({
                    "event": "message_deleted",
                    "message_id": message_id
                }))

    @sync_to_async
    def update_last_seen(self):
        profile, created = UserProfile.objects.get_or_create(user=self.user)
        profile.last_seen = datetime.now()
        profile.save()
