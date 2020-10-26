from flask import Blueprint, render_template
from .models import Item

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)
