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
    searchArgs = request.args['search']
    noResult = ""
    if searchArgs:
        items = "%" + searchArgs + '%'
        if Item.query.filter(Item.name.like(items)).all() != None:
            filteredItems = Item.query.filter(Item.name.like(items)).all()
        else:
            noResult = "Sorry, no results for " + searchArgs
        return render_template('items_filtered.html', filteredItems=filteredItems, title=('Search: ' + searchArgs), noResult=noResult)
    else:   
        return redirect(url_for('main.index'))
