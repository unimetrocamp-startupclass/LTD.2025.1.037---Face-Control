from flask import Blueprint

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return {"message": "API está funcionando!"}
