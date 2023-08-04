import uuid

from sqlalchemy import String, Column, Text

from database import Base


class Board(Base):
    __tablename__ = 'board'

    id = Column(String(120), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(80), default='No title', nullable=False, index=True)
    content = Column(Text, nullable=True)
