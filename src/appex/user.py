from flask import Blueprint


bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/index", methods=(["get"]))
def index():
    return "index test"
