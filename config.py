from datetime import datetime

class CONFIG:
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://用户名:密码@端口/数据库'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # GitHub TOKEN配置(可扩充访问速率为5000次/h，否则速率为60次/h)
    TOKEN = 'XXXXXXX'

    # 设置收集的时间区间
    start = datetime(XX, X, X)
    end = datetime.today()

    # 设置收集地区
    location = ["XX", "XX"]

    # 设置收集周期(天数)
    cycles = X


