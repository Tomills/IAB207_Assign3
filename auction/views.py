from flask import Blueprint, render_template, request, redirect, url_for
from .models import Item
               
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    items = Item.query.all()
    recentitems = Item.query.order_by(Item.date_posted.desc()).limit(6)
    return render_template('index.html', items=items, recentitems=recentitems)


# route to allow users to search
@bp.route('/search', methods=['GET', 'POST'])
def search():
    if request.args['search']:
        items = "%" + request.args['search'] + '%'
        # itemsFiltered = Item.query.filter(Item.artist.like(items)).all()
        itemsFiltered = Item.query.filter_by(artist=items)
        return render_template('items_filtered.html', itemsFiltered=itemsFiltered, title='Search')
    else:   
        return redirect(url_for('main.index'))
