# DW_Homework_4
# นาย ปัณณวิชญ์ จิตพิมลวัฒน์ 65114540365

ข้อมูลที่ใช้ COVID-19 Open-Data
ทำการสร้างฐานข้อมูลเพื่อทำการรองรับขอมูลใน Clikhouse

ทำการ Insert ข้อมูลผ่านคำสั่งที่ปรากฏในลิงค์ (https://clickhouse.com/docs/getting-started/example-datasets/covid19)
เมื่อทำการเพิ่มข้อมูลเสร็จ ให้ทำการเปิด Sever Clickhouse(Docker) ด้วยคำสั่งดังนี้
1. docker run -d --name clickhouse-server -p 9000:9000 -p 8123:8123 yandex/clickhouse-server
2. docker exec -it clickhouse-server clickhouse-client


สร้างไฟล์ Views.py เพื่อทำการเชื่อมต่อและดึงข้อมูลมาแสดงผล
แสดงผลด้วย HTML (hw04.html)
จากนั้นทำการ python manage.py runserver
