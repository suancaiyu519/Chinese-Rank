from data.collect import data_collect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import CONFIG
from data.models import Base
from log_config import logger

# 创建数据库引擎
engine = create_engine(CONFIG.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

# 收集时间区间
start = CONFIG.start
end = CONFIG.end

if __name__ == '__main__':
    session = Session()
    logger.info("Github 国内项目收集开始!")
    try:
        Base.metadata.create_all(engine)
        data_collect(start, end, session)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        logger.info("Github 国内项目收集完成!")
        session.close()
