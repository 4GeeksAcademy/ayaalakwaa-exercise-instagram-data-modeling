import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(25), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)

class Followers(Base):
    __tablename__ = 'followers'
    follower_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship("Users")

class Comments(Base):
    __tablename__ = 'comments'
    comment_id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('users.user_id'))
    post_id = Column(Integer, ForeignKey('post.post_id'))
    user = relationship("Users")
    post = relationship("Post")

class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship("Users")
    comment = relationship("Comments")

class Media(Base):
    __tablename__ = 'media'
    media_id = Column(Integer, primary_key=True)
    media_url = Column(String(100), nullable=False)
    post_id = Column(Integer, ForeignKey('post.post_id'))
    post = relationship("Post")
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')