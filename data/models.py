from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, autoincrement=True)
    项目地址 = Column(String(255), unique=True)
    项目简介 = Column(Text)
    Star数量 = Column(Integer)
    Fork数量 = Column(Integer)
    开发语言 = Column(String(50))
    项目大小 = Column(Integer)
    作者昵称 = Column(String(255))
    作者姓名 = Column(String(255))
    作者所在地 = Column(String(255))
    作者粉丝数 = Column(Integer)
    项目创建时间 = Column(DateTime)

