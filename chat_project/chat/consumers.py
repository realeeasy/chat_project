import json
from channels.generic.websocket import AsyncWebsocketConsumer
import re

def sanitize_room_name(room_name):
    # 替换掉非 ASCII 字符，保留字母、数字、下划线、连字符和句点
    return re.sub(r'[^a-zA-Z0-9_-]', '_', room_name)
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # 从 URL 路由中获取房间名称
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # 定义群组名称（可以根据实际情况调整）
        self.room_group_name = f'chat_{self.room_name}'

        # 加入房间群组
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # 接受 WebSocket 连接
        await self.accept()

    async def disconnect(self, close_code):
        # 离开房间群组
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # 解析前端发送的 JSON 数据
        data = json.loads(text_data)
        message = data.get('message', '')
        # 这里可以从 self.scope 中获取登录用户信息
        username = self.scope["user"].username if self.scope.get("user") and self.scope["user"].is_authenticated else "Anonymous"

        # 将消息发送到房间群组
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',  # 指定调用 chat_message 方法处理
                'message': message,
                'username': username
            }
        )

    # 处理群组中发送的消息
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # 将消息发送到 WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
