from data.collect import data_collect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import CONFIG
from data.models import Base
import schedule
import time

# 创建数据库引擎
engine = create_engine(CONFIG.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

start = CONFIG.start
end = CONFIG.end


def job():
    session = Session()
    try:
        Base.metadata.create_all(engine)
        data_collect(start, end, session)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()


schedule.every(CONFIG.cycles).days.do(job)

if __name__ == '__main__':
    job()
    while True:
        schedule.run_pending()
        time.sleep(1)
