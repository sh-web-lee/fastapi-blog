from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime, Text
from sqlalchemy.orm import relationship

from databases.connect import Base


class User(Base):
    __tablename__ = 'users'
    uid = Column(String(length=50), primary_key=True, default=lambda: str(uuid4()))
    name = Column(String(length=50), unique=True, nullable=False)
    password = Column(String(length=50), nullable=False)
    is_active = Column(Boolean, default=True)
    create_time = Column(DateTime, default=datetime.now())
    email = Column(String(50), unique=True)
    # articles = relationship('Article', back_populates='users')
    # tags = relationship('Tag', back_populates='users')


class Article(Base):
    __tablename__ = 'articles'
    aid = Column(String(length=50), primary_key=True, default=lambda: str(uuid4()))
    create_time = Column(DateTime, default=datetime.now())
    last_update_time = Column(DateTime, default=datetime.now())
    title = Column(Text, nullable=False)
    body = Column(Text)
    path = Column(Text)
    # users = relationship('User', back_populates='articles')

class Tag(Base):
    __tablename__ = 'tags'
    tid = Column(String(length=50), primary_key=True, default=lambda: str(uuid4()))
    create_time = Column(DateTime, default=datetime.now())
    name = Column(String(length=50), unique=True, nullable=False)
    info = Column(Text)
    # users = relationship('User', back_populates='tags')


# 反向orm
if __name__=='__main__':
    from databases.connect import engine
    Base.metadata.create_all(bind=engine)