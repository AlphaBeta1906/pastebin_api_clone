from flask import Blueprint,jsonify,request,abort,redirect,url_for,current_app,Response
from ..model import Paste,pastes_schema,paste_schema
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
    pastes = Paste.query.all()
    if unique_id:
        paste = Paste.query.filter_by(unique_id=unique_id).first_or_404()
        return paste_schema.dump(paste)
    pastes =  pastes_schema.dump(pastes)
    return jsonify(pastes=pastes)

@paste.get("/pastes")
def page_paste():
    pages = 1 if not request.args.get("page") else int(request.args.get("page"))
    pastes = Paste.query.filter(Paste.unique_id != "").offset(get_start(pages,limit=10)).limit(10).all()
    pastes =  pastes_schema.dump(pastes)
    if not pastes:
        return abort(404)
    return jsonify(pastes=pastes)
    
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
    Lang = {
      "python": "py",
      "java": "java",
      "c": "c",
      "cpp": "cpp",
      "cs": "cs",
      "ruby": "ruby",
      "go": "go",
      "rust": "rs",
      "jsx": "jsx",
      "tsx": "tsx",
      "javascript": "js",
      "typescript": "ts",
      "haskell": "hs",
      "elm": "elm",
      "erlang": "erl",
      "elixir": "ex"
    }
    paste = Paste.query.filter_by(unique_id = unique_id).first_or_404()
    filename = None
    try:
        filename = f"{unique_id}.{Lang[paste.language]}"
    except KeyError:
        filename = f"{unique_id}.txt"
        
    return redirect(url_for("paste.download",filename = filename))

@paste.get("/dl/<filename>")
def download(filename):
    paste = Paste.query.filter_by(unique_id = filename.split(".")[0]).first_or_404()
    file = open(f"{paste.title}.txt","w")
    file.write(paste.code)
    return current_app.response_class(paste.code,mimetype = "text/file")    

@paste.get("/test")
def test():
    return jsonify(message="api connected")
