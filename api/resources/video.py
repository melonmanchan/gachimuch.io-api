__author__ = 'matti'

from common.database import db
import datetime

from flask import jsonify
from flask_restful import Resource
from models.video import VideoModel

class Video(Resource):
    def get(self, videoid):
        video = VideoModel.query.get_or_404(videoid)
        video.views += 1
        db.session.add(video)
        db.session.commit()
        resp = {'video': video.tojson()}
        return jsonify(resp)

    def post(self):
        video = VideoModel('title', 'desc', '12312445', 'http://asd123.com', datetime.datetime.now(),
                      datetime.datetime.now())
        db.session.add(video)
        db.session.commit()
        return  200
