__author__ = 'matti'
from app import db

## DB models in here for now, due to Python import problems...
class VideoModel(db.model):
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(80))
    description = db.Column(db.Text(500))
    nicoid      = db.Column(db.String(20), unique=True)
    videourl    = db.Column(db.String(100), unique=True)

    originalupload = db.Column(db.Date)
    reupload       = db.Column(db.Date)

    def __init__(self, title, description, nicoid, videourl, originalupload, reupload):
        self.title = title
        self.description = description
        self.nicoid = nicoid
        self.videourl = videourl
        self.originalupload = originalupload
        self.reupload = reupload