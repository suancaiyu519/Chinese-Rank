from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Projects(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    项目地址 = db.Column(db.String(255), unique=True)
    项目简介 = db.Column(db.Text)
    Star数量 = db.Column(db.Integer)
    Fork数量 = db.Column(db.Integer)
    开发语言 = db.Column(db.String(50))
    项目大小 = db.Column(db.Integer)
    作者昵称 = db.Column(db.String(255))
    作者姓名 = db.Column(db.String(255))
    作者所在地 = db.Column(db.String(255))
    作者粉丝数 = db.Column(db.Integer)


