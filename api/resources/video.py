__author__ = 'matti'

from app import db
import datetime

from flask import jsonify
from flask_restful import Resource
from models.video import VideoModel

class Video(Resource):
    def get(self):
        return {'video': 'test'}

    def post(self):
        video = VideoModel('title', 'desc', '12345', 'http://asd.com', datetime.datetime.now(),
                      datetime.datetime.now())
        db.session.add(video)
        db.session.commit()
        return jsonify(video), 200
        return 200

