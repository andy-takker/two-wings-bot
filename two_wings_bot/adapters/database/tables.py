from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from two_wings_bot.adapters.database.base import (
    BaseTable,
    IdentifableMixin,
    TimestampedMixin,
)


class Question(BaseTable, TimestampedMixin, IdentifableMixin):
    __tablename__ = "questions"

    question: Mapped[str] = mapped_column(String(511), nullable=False)
    answer: Mapped[str] = mapped_column(String(3071), nullable=False)
