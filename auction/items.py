from flask import Blueprint, render_template, request, redirect, url_for
from .models import Item
from . import db


bp = Blueprint('items', __name__, url_prefix='/items')

@bp.route('/<id>')
def show(id):
    if (id != "All"):
        filteredItems = Item.query.filter_by(genre=id)
    else:
        filteredItems = Item.query.all()
    return render_template('items_filtered.html', filteredItems=filteredItems, genre=id)