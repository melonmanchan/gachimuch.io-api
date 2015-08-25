__author__ = 'matti'
from common.database import db

class VideoModel(db.Model):
    __tablename__ = 'video'

    id          = db.Column(db.Integer, primary_key=True)
    views       = db.Column(db.Integer)
    title       = db.Column(db.String(80))
    description = db.Column(db.Text)
    nicoid      = db.Column(db.String(20), unique=True)
    videourl    = db.Column(db.String(100), unique=True)

    originalupload = db.Column(db.Date)
    reupload       = db.Column(db.Date)

    def __init__(self, title, description, nicoid, videourl, originalupload, reupload):
        self.title = title
        self.views = 0
        self.description = description
        self.nicoid = nicoid
        self.videourl = videourl
        self.originalupload = originalupload
        self.reupload = reupload

    def tojson(self):
        return {'id': self.id, 'title': self.title, 'description': self.description,
                'nicoid': self.nicoid, 'videourl': self.videourl, 'views': self.views,
                'originalupload': str(self.originalupload), 'reupload': str(self.reupload)}