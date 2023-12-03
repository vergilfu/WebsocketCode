from sqlalchemy import Column, Integer, String,Text,DateTime,func
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
import psycopg2

Base = declarative_base()
engine = create_engine('postgresql://postgres:123456@localhost:5432/postgres')


class Notebooks(Base):
    __tablename__ = 'notebooks'
    fid = Column(Integer, primary_key=True, autoincrement=True)
    ftitle = Column(String(255))
    fcontent = Column(Text)
    fcreatetime = Column(DateTime, default=func.now())
    fmodifytime = Column(DateTime, default=func.now(), onupdate=func.now())
    fnodename = Column(String(255))
    fnodeid = Column(Integer)
    fparentnodename = Column(String(255))
    fparentnodeid = Column(Integer)

if __name__ == '__main__':
    # 创建表
    Base.metadata.create_all(engine)