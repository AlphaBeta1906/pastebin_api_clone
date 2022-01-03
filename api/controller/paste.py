from flask import Blueprint,jsonify,request,abort,redirect,url_for
from ..model import Paste,pastes_schema,paste_schema

paste = Blueprint("paste", __name__)

@paste.get("/")
def main():
    return redirect(url_for("paste.get_paste"))    

@paste.get("/paste",defaults={"id":None})
@paste.get("/paste/<int:id>")
def get_paste(id):        
    if id:
        paste = Paste.query.filter_by(id=id).first_or_404()
        return paste_schema.dump(paste)
    pastes = Paste.query.all()
    pastes =  pastes_schema.dump(pastes)
    return jsonify(pastes=pastes)
    

@paste.post("/paste")
def new_paste():
    try:
        title = request.get_json()["title"]
        code = request.get_json()["code"]
        language = request.get_json()["language"]
    except KeyError:
        abort(400)
    paste = Paste(title=title,code=code,language=language) 
    paste.add()
    return jsonify(message="paste successfully created")
    
    
@paste.get("/test")
def test():
    return jsonify(message="api connected")
