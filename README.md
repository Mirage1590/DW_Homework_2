# DW_Homework_2
# นาย ปัณณวิชญ์ จิตพิมลวัฒน์ 65114540365

# A. วิธีการติดตั้งและเปิดใช้งาน ClickHouse

1. **ติดตั้ง Docker**:
   ก่อนอื่นคุณต้องติดตั้ง Docker บนเครื่องของคุณ:

   * ดาวน์โหลด Docker จาก [Docker Desktop](https://www.docker.com/products/docker-desktop)
   * ติดตั้ง Docker และเปิดใช้งาน
   * ตรวจสอบการติดตั้งด้วยคำสั่ง:

     ```bash
     docker --version
     ```

2. **ดาวน์โหลดและรัน ClickHouse ผ่าน Docker**:
   ใช้ Docker เพื่อรัน ClickHouse:

   ```bash
   docker run --name clickhouse-server -d --ulimit nofile=262144:262144 -p 8123:8123 -p 9000:9000 yandex/clickhouse-server
   ```

3. **ตรวจสอบการเชื่อมต่อ**:
   คุณสามารถทดสอบการเชื่อมต่อไปยัง ClickHouse ได้ผ่าน `clickhouse-client`:

   ```bash
   clickhouse-client --host localhost --port 9000
   ```

4. **เปิดใช้งาน ClickHouse**:

   * เข้าใช้งาน ClickHouse ผ่าน Web UI ที่ `http://localhost:8123`
   * ใช้คำสั่ง SQL เพื่อเชื่อมต่อและตรวจสอบข้อมูล


# B. วิธีการนำเข้าข้อมูลจากการบ้านที่ 4 (HW04)

  ทำการ Insert ข้อมูลผ่านคำสั่งที่ปรากฏในลิงค์ (https://clickhouse.com/docs/getting-started/example-datasets/covid19) เมื่อทำการเพิ่มข้อมูลเสร็จ ให้ทำการเปิด Sever Clickhouse(Docker) ด้วยคำสั่งดังนี้
  
    1.docker run -d --name clickhouse-server -p 9000:9000 -p 8123:8123 yandex/clickhouse-server
    2.docker exec -it clickhouse-server clickhouse-client

---

# C. เขียนวิธีการติดตั้งและเปิดใช้งาน superset

1. Get Superset
    git clone https://github.com/apache/superset

2. Start the latest official release of Superset
    # Enter the repository you just cloned
    $ cd superset

    # Set the repo to the state associated with the latest official version
    $ git checkout tags/5.0.0

    # Fire up Superset using Docker Compose
    $ docker compose -f docker-compose-image-tag.yml up

3. Login to Superset
  Now head over to http://localhost:8088 and log in with the default created account:

  username: admin
  password: admin

---

# D. วิธีการเชื่อม Superset กับ ClickHouse

1. **เปิดใช้งาน Superset**:
   เมื่อคุณเข้าใช้งาน Superset ผ่าน `http://localhost:8088`, ให้ล็อกอินด้วยข้อมูลผู้ใช้ที่ตั้งค่าไว้

2. **เพิ่มฐานข้อมูล ClickHouse**:

   * ไปที่หน้า "Data" > "Databases"
   * คลิกที่ "Add Database"
   * เลือก "ClickHouse" จากเมนูประเภทฐานข้อมูล
   * กรอกข้อมูลการเชื่อมต่อ:

     * **SQLAlchemy URI**: `clickhouse://default:@localhost:9000/default`
     * **Username**: `default` (หรือชื่อผู้ใช้ที่คุณตั้งไว้)
     * **Password**: รหัสผ่านที่ใช้เชื่อมต่อ

3. **ทดสอบการเชื่อมต่อ**:
   คลิกที่ "Test Connection" เพื่อทดสอบว่า Superset สามารถเชื่อมต่อกับฐานข้อมูล ClickHouse ได้

---

# E. วิธีการนำเสนอข้อมูลจากข้อมูล b. บน Dashboard ของ Superset พร้อมผลลัพธ์

1. **สร้าง Chart ใน Superset**:

   * ไปที่เมนู "Charts" > "Create a new chart"
   * เลือกฐานข้อมูลที่คุณเชื่อมต่อ (ClickHouse)
   * เลือกตารางที่คุณนำเข้าในขั้นตอนก่อนหน้า
   * เลือกรูปแบบการแสดงผล (เช่น Table, Bar chart, Line chart)

2. **เพิ่ม Chart ลงใน Dashboard**:

   * เมื่อสร้าง chart เสร็จแล้ว, ให้คลิกที่ "Save" และเพิ่มลงใน Dashboard
   * คุณสามารถสร้าง Dashboard ใหม่หรือเพิ่มลงใน Dashboard ที่มีอยู่แล้ว

3. **ทดสอบและแสดงผล**:

   * เปิด Dashboard ที่สร้างขึ้นใหม่
   * ตรวจสอบว่าแสดงผลข้อมูลจาก ClickHouse ได้อย่างถูกต้อง

<img width="1911" height="921" alt="image" src="https://github.com/user-attachments/assets/522e0026-1ccc-4c0e-a43c-fce62f523930" />

---

# F. บทสรุปการใช้งาน

1. **การติดตั้งและเปิดใช้งาน ClickHouse**:

   * ติดตั้ง **Docker** เพื่อใช้งาน ClickHouse ผ่าน Docker Container
   * รัน ClickHouse บน Docker และทดสอบการเชื่อมต่อผ่าน `clickhouse-client`
   * เปิดใช้งาน ClickHouse ผ่าน Web UI ที่ `http://localhost:8123` และใช้คำสั่ง SQL เพื่อเชื่อมต่อและตรวจสอบข้อมูล

2. **การนำเข้าข้อมูลจากการบ้านที่ 4 (HW04)**:

   * ข้อมูลจากการบ้าน HW04 ถูกนำเข้ามาใน ClickHouse ผ่านคำสั่งที่ระบุในเอกสารของ ClickHouse
   * ใช้คำสั่ง Docker เพื่อเปิดเซิร์ฟเวอร์ ClickHouse และใช้งาน `clickhouse-client` ในการเพิ่มข้อมูล

3. **การติดตั้งและเปิดใช้งาน Apache Superset**:

   * ติดตั้ง **Apache Superset** โดยการ clone repository จาก GitHub
   * รัน **Superset** ผ่าน Docker Compose และเข้าใช้งานที่ `http://localhost:8088` ด้วยข้อมูลล็อกอินเริ่มต้น

4. **การเชื่อมต่อ Superset กับ ClickHouse**:

   * เพิ่มฐานข้อมูล **ClickHouse** ใน Superset โดยกรอกข้อมูลการเชื่อมต่อผ่าน SQLAlchemy URI
   * ทดสอบการเชื่อมต่อเพื่อให้แน่ใจว่า Superset สามารถเชื่อมต่อกับ ClickHouse ได้สำเร็จ

5. **การนำเสนอข้อมูลบน Dashboard ของ Superset**:

   * สร้าง **Chart** ใน Superset โดยใช้ข้อมูลจาก ClickHouse
   * เพิ่ม Chart ลงใน Dashboard และสามารถเลือกประเภทการแสดงผลได้หลากหลาย เช่น ตาราง, กราฟแท่ง หรือกราฟเส้น
   * เปิด Dashboard ที่สร้างขึ้นใหม่และตรวจสอบการแสดงผลข้อมูลจาก ClickHouse
---
