from flask import Flask
from config import CONFIG
from app.models import db
from app.route import register_routes
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = CONFIG.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = CONFIG.SQLALCHEMY_TRACK_MODIFICATIONS

with app.app_context():
    db.init_app(app)
    register_routes(app, db)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
