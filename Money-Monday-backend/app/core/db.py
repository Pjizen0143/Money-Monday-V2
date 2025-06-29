from typing import Annotated

from sqlmodel import create_engine, Session, SQLModel
from fastapi import Depends

from app import models # noqa: F401
# เพื่อให้ engine รู้จัก model ที่เราจะใช้สร้างตาราง database

postgresql_url = 'postgresql://username:password@localhost/database'

engine = create_engine(postgresql_url)
# engine คือเครื่องมือที่ใช้เชื่อมต่อกับฐานข้อมูล
# ทำหน้าที่แปลงคำสั่ง ORM เป็นคำสั่ง SQL ที่ฐานข้อมูลเข้าใจ
# เราต้องระบุ URL ของฐานข้อมูลเพื่อให้ engine รู้ว่าจะเชื่อมต่อที่ไหน


def get_session():
    # ฟังก์ชันสำหรับสร้าง session ใช้เชื่อมต่อกับฐานข้อมูลชั่วคราว
    # Session ทำหน้าที่จัดการคำสั่งต่าง ๆ เช่น SELECT, INSERT, UPDATE, DELETE
    with Session(engine) as session:
        # ภายใน with จะเปิด session และปิดให้อัตโนมัติหลังใช้งาน
        yield session

SessionDep = Annotated[Session, Depends(get_session)]


def get_session_local() -> Session:
    return Session(engine)

SessionLocal = get_session_local()


def init_db():
    # ใช้สร้างตาราง database

    SQLModel.metadata.create_all(engine)

