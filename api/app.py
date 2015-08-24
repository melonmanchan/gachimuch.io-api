__author__ = 'matti'
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from resources.video import Video
from flask_restful import Api
## Resources
db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

api = Api(app)
api.add_resource(Video, '/video')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
