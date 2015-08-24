__author__ = 'matti'
from flask import Flask
from resources.video import Video
from flask_restful import Api
from common.database import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    api = Api(app)
    api.add_resource(Video, '/video')
    db.init_app(app)
    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
