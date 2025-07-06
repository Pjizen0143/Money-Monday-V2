from sqlmodel import Session, select

from app.models.user import User, UserCreate
from app.models.common import Message
from app.core.security import verify_password, get_password_hash

def create_user(*, session: Session, user_create: UserCreate) -> User:
    db_object = User.model_validate(
        user_create, update={"hashed_password": get_password_hash(user_create.password)}
    )
    # db_object คือข้อมูลที่เราจะนำเข้า database โดยใช้ model User
    # รับ input จาก model UserCreate
    # แปลง password เป็นแบบ hash ก่อนแล้วค่อยนำเข้า

    session.add(db_object)  # เตรียมใส่ข้อมูลลง database
    session.commit()  # ยืนยัน บันทึกลง dataabse จริง
    session.refresh(db_object)  # ดึงค่าล่าสุดกลับมา เช่น id ที่เพิ่งถูกสร้าง
    return db_object


def delete_user(*, session: Session, user: User) -> Message:
    session.delete(user)
    session.commit()
    return Message(message="User deleted!")


def get_user_by_email(*, session: Session, email: str) -> User | None:
    statement = select(User).where(User.email == email)
    session_user = session.exec(statement).first() # type: ignore
    return session_user


def get_user_by_username(*, session: Session, username: str) -> User | None:
    statement = select(User).where(User.username == username)
    session_user = session.exec(statement).first() # type: ignore
    return  session_user


def authenticate(*, session: Session, username__or_email: str, password: str) -> User | None:
    db_object = get_user_by_email(session=session, email=username__or_email)

    if not db_object:
        db_object = get_user_by_username(session=session, username=username__or_email)

    if not db_object:
        return None
    if not verify_password(password, db_object.hashed_password):
        return None
    return db_object
