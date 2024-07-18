from data.collect import data_collect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import CONFIG
from data.models import Base

# 创建数据库引擎
engine = create_engine(CONFIG.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

start = CONFIG.start
end = CONFIG.end

if __name__ == '__main__':
    # 创建所有表
    Base.metadata.create_all(engine)
    data_collect(start, end, session)
    session.close()
