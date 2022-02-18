from flask import jsonify,abort
from sqlalchemy.sql import func

from . import db,marshmallow

class PasteSchema(marshmallow.Schema):
    class Meta:
        # Fields to expose
        fields = ("id","title", "code", "language", "date_created","unique_id")

class Paste(db.Model):
    """table where code/posts are stored"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    code = db.Column(db.String(10000), nullable=False)    
    language = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    unique_id = db.Column(db.String(10),nullable=False)
    
    paste_schema = PasteSchema()
    pastes_schema = PasteSchema(many=True)    
    
    def __init__(self,id=None,title=None,code=None,language=None,unique_id=None):
            self.id = id
            self.title = title
            self.code = code
            self.language = language
            self.unique_id = unique_id
    def add(self):
        db.session.add(self)
        db.session.commit()
    def get_paste_desc_paged(self,offset,_language=None):
        pastes = (self.query
                     .filter(Paste.unique_id != "")
                     .order_by(Paste.id.desc())
                     .offset(offset)
                     .limit(10)
                     .all()
               )
        if _language:
            pastes = (self.query
                     .filter(Paste.unique_id != "")
                     .filter_by(language=_language)
                     .order_by(Paste.id.desc())
                     .offset(offset)
                     .limit(10)
                     .all()
               )            
        return self.pastes_schema.dump(pastes)
    def get_paste_paged(self,offset,_language=None):
        pastes =  (self.query
                     .filter(Paste.unique_id != "")
                     .offset(offset)
                     .limit(10)
                     .all()
               ) 
        print(_language)
        if _language:
            pastes = (self.query
                     .filter(Paste.unique_id != "")
                     .filter_by(language=_language)
                     .offset(offset)
                     .limit(10)
                     .all()
               )          
        return self.pastes_schema.dump(pastes)           
    def get_all(self):
        pastes = self.query.all()
        return self.pastes_schema.dump(pastes)
    def get_one(self,unique_id):
        paste = self.query.filter_by(unique_id=unique_id).first_or_404()
        return self.paste_schema.dump(paste)