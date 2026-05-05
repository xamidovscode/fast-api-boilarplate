__all__ =(
    'User',
)

from sqlalchemy import String, Integer, Boolean, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.choices import UserRoles


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
    phone: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        comment="User's phone number",
    )
    role: Mapped[UserRoles] = mapped_column(
        SqlEnum(UserRoles),
        default=UserRoles.seller,
        server_default='seller',
        nullable=False,
        comment="User's role",
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        comment="Whether the user is active",
    )


