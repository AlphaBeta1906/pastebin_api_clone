from flask import jsonify,abort
from sqlalchemy.sql import func

from . import db,marshmallow


class Paste(db.Model):
    """table where code/posts are stored"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    code = db.Column(db.String(10000), nullable=False)    
    language = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    unique_id = db.Column(db.String(10),nullable=False)
    def __init__(self,id=None,title=None,code=None,language=None,unique_id=None):
            self.id = id
            self.title = title
            self.code = code
            self.language = language
            self.unique_id = unique_id
    def add(self):
        db.session.add(self)
        db.session.commit()


class PasteSchema(marshmallow.Schema):
    class Meta:
        # Fields to expose
        fields = ("id","title", "code", "language", "date_created","unique_id")
    
paste_schema = PasteSchema()
pastes_schema = PasteSchema(many=True)

