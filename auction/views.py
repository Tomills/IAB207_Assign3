from flask import Blueprint, render_template
from .models import Item
from datetime import date
bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    today = date.today()
    items = Item.query.all()
    recentitems = Item.query.order_by(Item.date_posted).limit(6)
    return render_template('index.html', items=items, recentitems=recentitems)
