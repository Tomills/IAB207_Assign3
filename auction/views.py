from flask import Blueprint, render_template
from .models import Item
bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    items = Item.query.all()
    recentitems = Item.query.order_by(Item.date_posted).limit(6)
    return render_template('index.html', items=items, recentitems=recentitems)


