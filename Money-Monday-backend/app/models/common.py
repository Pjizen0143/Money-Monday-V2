from sqlmodel import SQLModel

# สำหรับ return ข้อความปกติ
class Message(SQLModel):
    message: str

# สำหรับรับ Json Token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"
