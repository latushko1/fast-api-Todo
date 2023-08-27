from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base, engine


class TodoItem(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    is_active = Column(Boolean, default=False)



