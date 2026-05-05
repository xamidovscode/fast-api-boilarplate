__all__ =(
    'User',
)

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Column, Integer, DateTime, Boolean, ForeignKey
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment="The primary key of the user",
    )
    username: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        comment="Username",
    )
    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="User's full name",
    )
    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="User's password",
    )
    phone: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
        comment="User's phone number",
    )


