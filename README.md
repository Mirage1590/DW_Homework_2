# DW_Homework_2
# นาย ปัณณวิชญ์ จิตพิมลวัฒน์ 65114540365

โปรเจคนี้เป็นตัวอย่างการใช้งาน Django ร่วมกับ ClickHouse สำหรับการประมวลผลข้อมูลเรียลไทม์ โดยจะดึงข้อมูลจาก ClickHouse และส่งข้อมูลผ่าน WebSocket ให้กับผู้ใช้งานที่เชื่อมต่ออยู่

ความต้องการ
- Docker
- Python 3.8+
- Django 5.2+
- Channels 3.0+
- ClickHouse Docker image

ขั้นตอนการติดตั้งและใช้งาน

1. Clone Repository
เริ่มต้นด้วยการ clone โปรเจคจาก GitHub มาที่เครื่องของคุณ

bash
git clone https://github.com/Mirage1590/DW_Homework_2.git

cd Data_Warehousing

2. ติดตั้ง Docker และรัน ClickHouse
โปรเจคนี้ใช้ ClickHouse ผ่าน Docker เพื่อจัดเก็บข้อมูล ในการใช้งานโปรเจคคุณจะต้องรัน ClickHouse ใน Docker
ใช้คำสั่งนี้เพื่อดึงและรัน ClickHouse ผ่าน Docker

bash
docker run -d --name clickhouse-server -p 8123:8123 -p 9000:9000 clickhouse/clickhouse-server

3. ติดตั้ง Dependencies ของ Python
ติดตั้ง dependencies ที่จำเป็นสำหรับโปรเจคนี้ โดยใช้คำสั่ง

bash
pip install -r requirements.txt

4. ทำการ Migrate ฐานข้อมูล
โปรเจคนี้ใช้ฐานข้อมูล SQLite ในการจัดเก็บข้อมูลต่างๆ ดังนั้นคุณจะต้องทำการ migrate ฐานข้อมูลก่อนใช้งาน

bash
python manage.py migrate

5. รัน Django Development Server
รันเซิร์ฟเวอร์ Django เพื่อทดสอบโปรเจค

bash
python manage.py runserver
