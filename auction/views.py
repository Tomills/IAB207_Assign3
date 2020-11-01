from flask import Blueprint, render_template, request, redirect, url_for
from .models import Item, Watchlist
from sqlalchemy import or_
from flask_login import current_user

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    user_id = current_user.get_id()
    items = Item.query.all()
    recentitems = Item.query.with_entities(Item.id, Item.name, Item.description, Item.artist, Item.genre, Item.year, Item.designation, Item.image, Item.starting_value, Item.current_value, Item.bid_number, Item.status, Item.user_id, Item.date_posted, Watchlist.id.label("watchlist_id")).outerjoin(Watchlist).filter(or_(Watchlist.user_id==user_id, Watchlist.user_id == None)).order_by(Item.date_posted.desc()).limit(6)
    popularitems = Item.query.order_by(Item.bid_number.desc()).limit(6)
    return render_template('index.html', items=items, recentitems=recentitems, popularitems=popularitems)


# route to allow users to search
@bp.route('/search', methods=['GET', 'POST'])
def search():
    searchArgs = request.args['search']
    noResult = ""
    if searchArgs:
        items = "%" + searchArgs + '%'
        filteredItems = ""
        if len(Item.query.filter(Item.name.like(items)).all()) != 0:
            filteredItems = Item.query.filter(Item.name.like(items)).all()
        elif len(Item.query.filter(Item.artist.like(items)).all()) != 0 :
            filteredItems = Item.query.filter(Item.artist.like(items)).all()
        elif len(Item.query.filter(Item.genre.like(items)).all()) != 0 :
            filteredItems = Item.query.filter(Item.genre.like(items)).all()
        else:
            noResult = "Sorry, no results for: " + searchArgs
        return render_template('items_filtered.html', filteredItems=filteredItems, title=('Search: ' + searchArgs), noResult=noResult)
    else:   
        return redirect(url_for('main.index'))
