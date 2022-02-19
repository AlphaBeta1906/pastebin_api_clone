from flask import Blueprint,jsonify,request,abort,redirect,url_for,current_app,Response
from ..model import Paste
from .. import cache

paste = Blueprint("paste", __name__)


def get_unique_id():
    import random
    import string

    unique_id = "".join(random.choices(string.ascii_lowercase + string.digits, k=4))
    return unique_id

def get_start(page, limit=10):
    """
    get start of query by page number
    """
    start = 0
    if page > 1:
        start = page * limit - limit
    return start


@paste.get("/")
def main():
    return redirect(url_for("paste.get_paste"))    

@paste.get("/paste/",defaults={"unique_id":None})
@paste.get("/paste/<unique_id>")
@cache.cached(timeout=60)
def get_paste(unique_id):
    _paste = Paste()
    if unique_id:
        return _paste.get_one(unique_id)
    pastes = _paste.get_all()
    return jsonify(pastes=pastes)

@paste.get("/pastes",defaults={"sort":"latest","language": None})
@paste.get("/pastes/<sort>",defaults={"language": None})
@paste.get("/pastes/<language>",defaults={"sort":"latest"})
@paste.get("/pastes/<sort>/<language>")
def page_paste(language,sort):
    pages = 1 if not request.args.get("page") else int(request.args.get("page"))
    pastes = Paste()
    start = get_start(pages,limit=10)
    _sort = {
        "latest":pastes.get_paste_desc_paged,
        "oldest":pastes.get_paste_paged
    }
    print(sort)
    print(language)
    _pastes = _sort[sort](start,language)
    return jsonify(pastes=_pastes)
    
@paste.post("/paste")
def new_paste():
    try:
        title = request.get_json()["title"]
        code = request.get_json()["code"]
        language = request.get_json()["language"]
    except KeyError:
        abort(400)
    unique_id = get_unique_id()
    paste = Paste(title=title,code=code,language=language,unique_id=unique_id) 
    paste.add()
    return jsonify(message="paste successfully created",unique_id=unique_id)
    
@paste.get("/paste/download/<unique_id>")
def download_paste(unique_id):
    paste = Paste.query.filter_by(unique_id = unique_id).first_or_404()
    filename = None
    try:
        filename = f"{unique_id}.{paste.language}"
    except KeyError:
        filename = f"{unique_id}.txt"
        
    return redirect(url_for("paste.download",filename = filename))

@paste.get("/dl/<filename>")
def download(filename):
    paste = Paste.query.filter_by(unique_id = filename.split(".")[0]).first_or_404()
    return current_app.response_class(paste.code,mimetype = "text/file")    

@paste.get("/test")
def test():
    return jsonify(message="api connected")
