# ルーティング
# /blogs にHTTPメソッドがGETでアクセスしたblogs関数を実行する
from flask import Blueprint

blog_bp = Blueprint("blog", __name__)

@blog_bp.route("/blogs")
def blogs():
    from flask import render_template 
    from .db import query_db
    blogs = query_db("SELECT * FROM blogs")

    # テンプレートにblogs変数を渡す
    return render_template('blogs.html', blogs = blogs)