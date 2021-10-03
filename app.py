from flask import Flask, redirect, url_for, request, abort, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

app = Flask(__name__)
db = SQLAlchemy(app, session_options={"autoflush": False})
migrate = Migrate(app, db)
ma = Marshmallow(app)
app.config["SECRET_KEY"] = os.urandom(128)
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 86400
app.config["SQLALCHEMY_POOL_SIZE"] = 200
app.config["SQLALCHEMY_POOL_RECYCLE"] = 100
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://pastebinCloneApi:farizi1234@pastebinCloneApi.mysql.pythonanywhere-services.com/ pastebinCloneApi$pasteBin
"


@app.errorhandler(404)
def _404(e):
    return (
        jsonify({"message": "url not found or empty/invalid parameter", "status": 404}),
        404,
    )


@app.errorhandler(500)
def _500(e):
    return jsonify({"message": "server eror", "status": 500}), 500


class Codes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unique_id = db.Column(db.String(1000), nullable=False)
    code_title = db.Column(db.String(1000), nullable=False)
    code = db.Column(db.String(10000), nullable=False)
    languange = db.Column(db.String(1000), nullable=False)
    date_added = db.Column(db.DateTime(), default=datetime.today(), nullable=False)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/get_code/<id>", methods=["GET"])
def get_code(id):
    code = Codes.query.filter_by(unique_id=id).first()
    if not code:
        abort(404)
    markdown = f"""

```{code.languange}
{code.code}
```
    """
    html = f"""
<pre>
    <code>
        {code.code}
    <code>
</pre>
    """

    return jsonify(
        {
            "code_title": code.code_title,
            "code": code.code,
            "languange": code.languange,
            "markdown_code_block": markdown,
            "date_added": code.date_added,
        }
    )


@app.route("/add_code", methods=["POST"])
def add_code():
    import random
    import string

    code_title = request.args.get("code_title")
    code = request.args.get("code")
    languange = request.args.get("languange")

    length = 4
    unique_id = "".join(
        random.choices(string.ascii_lowercase + string.digits, k=length)
    )
    add = Codes(
        code_title=code_title, code=code, languange=languange, unique_id=unique_id
    )
    db.session.add(add)
    db.session.commit()
    return jsonify(
        {
            "message": "successfully added code",
            "code_url": url_for("get_code", id=unique_id),
        }
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
