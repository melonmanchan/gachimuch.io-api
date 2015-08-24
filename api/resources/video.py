__author__ = 'matti'

from common.database import db
import datetime

from flask import jsonify
from flask_restful import Resource
from models.video import VideoModel

class Video(Resource):
    def get(self, videoid):
        resp = VideoModel.query.get_or_404(videoid).tojson()
        return jsonify(resp)

    def post(self):
        video = VideoModel('title', 'desc', '12312445', 'http://asd123.com', datetime.datetime.now(),
                      datetime.datetime.now())
        db.session.add(video)
        db.session.commit()
        return  200
