import logging
from logging.handlers import TimedRotatingFileHandler

# 创建一个logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # 设置日志级别

# 创建一个TimedRotatingFileHandler，用于日志文件的定时轮换
# 'when'参数设置为'midnight'表示每天午夜轮换日志文件
# 'interval'参数设置为1表示每天轮换一次
# 'backupCount'参数设置为7表示保留7个备份文件
handler = TimedRotatingFileHandler('log/collect.log', when='midnight', interval=1, backupCount=7)

# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# 将formatter应用到handler
handler.setFormatter(formatter)

# 将handler添加到logger
logger.addHandler(handler)

