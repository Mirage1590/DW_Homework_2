import json
from channels.generic.websocket import AsyncWebsocketConsumer
from clickhouse_connect import get_client

class EventConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        client = get_client(host='localhost')

        # ดึงจำนวนเหตุการณ์จากฐานข้อมูล
        result = client.query('SELECT count() FROM events')
        count = result.result_rows[0][0]

        # เพิ่มจำนวนเหตุการณ์
        count += 1  # เพิ่มจำนวนเหตุการณ์ทุกครั้งที่มีการเชื่อมต่อ

        # ส่งข้อมูลจำนวนเหตุการณ์ที่อัปเดตไปยัง client
        await self.send(text_data=json.dumps({'count': count}))
